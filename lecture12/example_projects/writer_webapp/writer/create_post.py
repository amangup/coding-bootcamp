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
    article_id = request.args.get('article_id')
    article = None
    if article_id:
        article = Article.query.get(article_id)
        if not article:
            return _article_not_found()
        if article.author_id != current_user.id:
            # In case someone is trying to edit another author's article,
            # just redirect to home page without any notice.
            return redirect(url_for('all_posts'))

    form = CreatePostForm(request.form)
    if request.method == 'POST':
        try:
            return _add_post_to_db(form, article)
        except SQLAlchemyError:
            flash("We couldn't add your article due to a technical issue"
                  " on our side. Please try again later.")
    elif article:
        form.title.data = article.article_title
        form.text.data = article.article_text

    return _render_form(form)


def _add_post_to_db(form, article):
    is_draft = True if form.save.data else False
    publish_date = None if is_draft else datetime.now(timezone.utc)

    if not is_draft and not form.validate():
        flash("Not all required fields were filled.")
        return _render_form(form)

    if article is None:
        article_id = token_urlsafe(16)
        article = Article(id=article_id,
                          article_title=form.title.data,
                          article_text=form.text.data,
                          author_id=current_user.id,
                          publish_date=publish_date)
        db.session.add(article)
    else:
        article_id = article.id
        article.article_title = form.title.data
        article.article_text = form.text.data
        article.publish_date = publish_date

    db.session.commit()

    if is_draft:
        flash("The article was saved as a draft.")
        return _render_form(form)
    else:
        return redirect(url_for('view_post', id=article_id))


def _render_form(form):
    return render_template('create_post.html', form=form)


def _article_not_found():
    return "Article Not Found", 404