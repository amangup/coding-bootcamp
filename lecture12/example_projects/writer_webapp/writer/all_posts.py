from flask import render_template

from writer import app
from writer.db_tables import Article


@app.route('/')
def all_posts():
    articles = Article.query.filter(Article.publish_date.isnot(None)).all()
    return render_template("posts_list.html", articles=articles)
