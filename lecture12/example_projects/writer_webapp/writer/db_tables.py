from flask_login import UserMixin
from writer import db, bcrypt


class User(UserMixin, db.Model):
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password_hash = db.Column(db.String(56), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    # We store the list of authors being followed as a JSON list of user ids
    following = db.Column(db.Text)

    articles_written = db.relationship("Article", lazy=True, backref="author")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def hash_password(cls, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return"{0}: {1}".format(self.email, self.name)


class Article(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    article_title = db.Column(db.Text)
    article_text = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    publish_date = db.Column(db.TIMESTAMP(timezone=True))

    def __repr__(self):
        return "{0}: {1}".format(self.id, self.article_title)
