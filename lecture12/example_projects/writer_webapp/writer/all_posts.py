import json

from flask import render_template
from flask_login import current_user, login_required
from sqlalchemy import desc

from writer import app
from writer.db_tables import Article


@app.route('/')
def all_posts():
    articles = Article.query.filter(Article.publish_date.isnot(None))\
        .order_by(desc(Article.publish_date))\
        .all()
    return render_template("posts_list.html", articles=articles)


@app.route('/following')
@login_required
def following():
    authors_following = []
    if current_user.following is not None:
        authors_following = json.loads(current_user.following)

    articles = Article.query.filter(Article.publish_date.isnot(None)) \
        .filter(Article.author_id.in_(authors_following)) \
        .order_by(desc(Article.publish_date)) \
        .all()
    return render_template("posts_list.html", articles=articles)

