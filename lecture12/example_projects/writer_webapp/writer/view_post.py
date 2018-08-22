from flask import request, render_template

from writer import app
from writer.db_tables import Article


@app.route('/post', methods=['GET'])
def view_post():
    article_id = request.args.get('id')
    if article_id is None:
        return _article_not_found()

    article = Article.query.get(article_id)
    if article is None or article.publish_date is None:
        return _article_not_found()

    return render_template("view_post.html", article=article)


def _article_not_found():
    return "Article Not Found", 404
