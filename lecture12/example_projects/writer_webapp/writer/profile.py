import sys

from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from writer import app, db
from writer.db_tables import Article
from writer.forms import ProfileUpdateForm, ArticleUpdateForm


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile_form = ProfileUpdateForm(request.form)
    article_update_form = ArticleUpdateForm(request.form)

    if request.method == 'POST':
        try:
            if profile_form.update.data:
                _update_profile_data(profile_form)
            elif article_update_form.edit.data:
                return _edit_article(article_update_form.article_id.data)
            elif article_update_form.delete.data:
                _delete_article(article_update_form.article_id.data)
        except SQLAlchemyError:
            flash("Unable to update due to a technical issue. "
                  "Please try again later.")

    return _render_profile_page()


def _render_profile_page():
    profile_form = ProfileUpdateForm()
    profile_form.name.data = current_user.name
    profile_form.email.data = current_user.email

    articles = current_user.articles_written.copy()
    articles.sort(reverse=True,
                  key=lambda a: a.publish_date.timestamp() if a.publish_date else sys.maxsize)

    article_update_forms = []
    for article in articles:
        article_update_form = ArticleUpdateForm()
        article_update_forms.append(article_update_form)
        article_update_form.article_id.data = article.id

    return render_template("profile.html", profile_form=profile_form,
                           article_update_forms=article_update_forms,
                           articles=articles)


def _update_profile_data(profile_form):
    if profile_form.name.data:
        current_user.name = profile_form.name.data

    if profile_form.email.data:
        current_user.email = profile_form.email.data

    db.session.commit()


def _delete_article(article_id):
    Article.query.filter(Article.id == article_id).delete()
    db.session.commit()


def _edit_article(article_id):
    return redirect(url_for('create_post', article_id=article_id))
