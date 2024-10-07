"""Insert sample data

Revision ID: 68bbbd73ef5b
Revises: 
Create Date: 2024-10-06 18:59:34.129070

"""
from alembic import op
import sqlalchemy as sa
from core import db
from core.models.users import Users
from core.models.jobs import Jobs
from core.constants.constant import ExperienceLevelEnum, JobTypeEnum
import json


# revision identifiers, used by Alembic.
revision = '68bbbd73ef5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True,
                autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('skills', sa.Text(), nullable=False),
        sa.Column('experience_level', sa.Enum(ExperienceLevelEnum,
                                            name='experiencelevelfield'), nullable=True),
        sa.Column('desired_roles', sa.Text(), nullable=True),
        sa.Column('locations', sa.Text(), nullable=True),
        sa.Column('job_type', sa.Enum(
            JobTypeEnum, name='jobtypefield'), nullable=True)
    )


    op.create_table('jobs',
        sa.Column('id', sa.Integer(), primary_key=True,
                    autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('required_skills', sa.Text(), nullable=False),
        sa.Column('experience_level', sa.Enum(ExperienceLevelEnum,
                                                name='experiencelevelfield'), nullable=True),
        sa.Column('location', sa.String(length=255), nullable=True),
        sa.Column('job_type', sa.Enum(
            JobTypeEnum, name='jobtypefield'), nullable=True),
        sa.Column('company', sa.String(length=255), nullable=False)
    )
    user_1 = Users(name='John Doe', skills=json.dumps('Python, Flask, SQLAlchemy'), experience_level=ExperienceLevelEnum.SENIOR, desired_roles=json.dumps('Python Developer, Data Analyst'), locations=json.dumps('New York, San Francisco'), job_type=JobTypeEnum.FULL_TIME)
    db.session.add(user_1)
    db.session.flush()
    
    job_1 = Jobs(title='Python Developer', company='ABC Corp', required_skills=json.dumps(['Python', 'Flask', 'SQLAlchemy']),
                 experience_level=ExperienceLevelEnum.SENIOR.value, location='New York', job_type=JobTypeEnum.FULL_TIME.value)
    job_2 = Jobs(title='Data Analyst', company='XYZ Inc', required_skills=json.dumps(['Python', 'Pandas', 'SQL']),
                 experience_level=ExperienceLevelEnum.JUNIOR.value, location='Delhi', job_type=JobTypeEnum.FULL_TIME.value)
    job_3 = Jobs(title='Software Engineer', company='123 Tech', required_skills=json.dumps(['Java', 'Spring', 'Hibernate']),
                 experience_level=ExperienceLevelEnum.SENIOR.value, location='Remote', job_type=JobTypeEnum.FULL_TIME.value)
    db.session.add(job_1)
    db.session.add(job_2)
    db.session.add(job_3)
    db.session.flush()
    
    db.session.commit()
def downgrade():
    pass
