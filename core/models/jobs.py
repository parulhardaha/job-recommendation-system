from core.server import db
from core.constants import constant
from sqlalchemy.types import Enum as BaseEnum


class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    experience_level = db.Column(BaseEnum(constant.ExperienceLevelEnum))

    def __repr__(self):
        return '<Jobs %r>' % self.id


# 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
