from core import db
from core.constants import constant
from sqlalchemy.types import Enum as BaseEnum

class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    required_skills = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    job_type = db.Column(BaseEnum(constant.JobTypeEnum), nullable=False)
    experience_level = db.Column(BaseEnum(constant.ExperienceLevelEnum), nullable=False)

    def __repr__(self):
        return '<Jobs %r>' % self.id

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def get_jobs(cls, _skills=None, _experience_level=None, _desired_roles=None, _locations=None, _job_type=None):
        # Create a list to hold all filter conditions
        filters = []

        # Filter by experience level
        if _experience_level:
            filters.append(cls.experience_level == _experience_level)

        # Filter by job type
        if _job_type:
            filters.append(cls.job_type == _job_type)

        # Filter by desired roles (titles)
        if _desired_roles:
            filters.append(cls.title.in_(_desired_roles))

        # Filter by locations
        if _locations:
            filters.append(cls.location.in_(_locations))

        # Apply all filters using the filter method and return the result
        return cls.filter(*filters).all()
    
    @classmethod
    def get_all_jobs(cls):
        return cls.query.all()
