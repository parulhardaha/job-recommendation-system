from core import db
from core.constants import constant
from sqlalchemy.types import Enum as BaseEnum


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    experience_level = db.Column(BaseEnum(constant.ExperienceLevelEnum), nullable=False)
    desired_roles = db.Column(db.Text, nullable=True)
    locations = db.Column(db.Text, nullable=True)
    job_type = db.Column(BaseEnum(constant.ExperienceLevelEnum), nullable=True)

    def __repr__(self):
        return '<Users %r>' % self.id
