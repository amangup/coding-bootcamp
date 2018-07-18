from quiz import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text)
    option_a = db.Column(db.Text)
    option_b = db.Column(db.Text)
    option_c = db.Column(db.Text)
    option_d = db.Column(db.Text)
    answer = db.Column(db.Integer)

    def __repr__(self):
        return "Q{0}: {1}".format(self.id, self.question_text)

