import json

from flask import request, render_template, flash
from flask_login import current_user
from markdown2 import markdown
from sqlalchemy.exc import SQLAlchemyError

from writer import app, db
from writer.db_tables import Article
from writer.forms import FollowAuthorForm


@app.route('/post', methods=['GET', 'POST'])
def view_post():
    article_id = request.args.get('id')
    if article_id is None:
        return _article_not_found()

    article = Article.query.get(article_id)
    if article is None or article.publish_date is None:
        return _article_not_found()

    author_followed = False
    form = FollowAuthorForm(request.form)
    if current_user.is_authenticated:
        following = []
        if current_user.following is not None:
            following = json.loads(current_user.following)

        if request.method == 'POST':
            try:
                if form.follow.data:
                    _follow_author(article.author_id, following)
                elif form.unfollow.data:
                    _unfollow_author(article.author_id, following)
            except SQLAlchemyError:
                flash("Unable to execute follow/unfollow author action due to a"
                      "technical issue. Please try again later.")

        if article.author_id in following:
            author_followed = True

    article_text_markdown = markdown(article.article_text)

    return render_template("view_post.html", article=article, article_text=article_text_markdown,
                           form=form, following=author_followed)


def _follow_author(author_id, following):
    if author_id not in following:
        following.append(author_id)
        _update_user_table(json.dumps(following))


def _unfollow_author(author_id, following):
    if author_id in following:
        following.remove(author_id)
        _update_user_table(json.dumps(following))


def _update_user_table(following):
    current_user.following = following
    db.session.commit()


def _article_not_found():
    return "Article Not Found", 404
