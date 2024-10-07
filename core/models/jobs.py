"""
The `Jobs` model represents a job posting in the application. It has the following fields:

- `id`: The unique identifier for the job posting.
- `title`: The title of the job posting.
- `company`: The company that is posting the job.
- `required_skills`: A text field containing the skills required for the job.
- `location`: The location of the job.
- `job_type`: The type of job, which is an enumeration value from the `constant.JobTypeEnum` class.
- `experience_level`: The required experience level for the job, which is an enumeration value from the `constant.ExperienceLevelEnum` class.

The `filter` class method allows filtering the `Jobs` model based on various criteria, such as experience level, job type, desired roles, locations, and skills.

The `get_jobs` class method is a convenience method that applies the various filters and returns the matching job postings.

The `get_all_jobs` class method returns all job postings.
"""
from core import db
from core.constants import constant
from sqlalchemy.types import Enum as BaseEnum
from sqlalchemy.exc import SQLAlchemyError

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
        try:

            # Filter by experience level
            if _experience_level:
                filters.append(cls.experience_level == _experience_level)

            # Filter by job type
            if _job_type:
                filters.append(cls.job_type == _job_type)

            # Filter by desired roles (titles)
            if _desired_roles:
                if not isinstance(_desired_roles, list):
                    return {"error": "Desired roles must be a list."}, 400
                filters.append(cls.title.in_(_desired_roles))

            # Filter by locations
            if _locations:
                if not isinstance(_locations, list):
                    return {"error": "Locations must be a list."}, 400
                filters.append(cls.location.in_(_locations))

            # Apply all filters using the filter method and return the result
            return cls.filter(*filters).all()

        except SQLAlchemyError as e:
            db.session.rollback()  # Rollback the session in case of error
            return {"error": f"Database error occurred: {str(e)}"}, 500
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}, 50
    
    @classmethod
    def get_all_jobs(cls):
        try:
            return cls.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": f"Database error occurred while fetching all jobs: {str(e)}"}, 500
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
