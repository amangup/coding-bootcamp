from datetime import datetime, timezone
from secrets import token_urlsafe

from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from writer import app, db
from writer.db_tables import Article
from writer.forms import CreatePostForm


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm(request.form)
    if request.method == 'POST':
        try:
            return _add_post_to_db(form)
        except SQLAlchemyError:
            flash("We couldn't add your article due to a technical issue"
                  " on our side. Please try again later.")

    return _render_form(form)


def _add_post_to_db(form):
    article_id = token_urlsafe(16)
    is_draft = True if form.save.data else False
    publish_date = None if is_draft else datetime.now(timezone.utc)

    if not is_draft and not form.validate():
        flash("Not all required fields were filled.")
        return _render_form(form)

    article = Article(id=article_id,
                      article_title=form.title.data,
                      article_text=form.text.data,
                      author_id=current_user.id,
                      publish_date=publish_date)
    db.session.add(article)
    db.session.commit()

    if is_draft:
        flash("The article was saved.")
        return _render_form(form)
    else:
        return redirect(url_for('view_post', id=article_id))


def _render_form(form):
    return render_template('create_post.html', form=form)
