"""Insert sample data

Revision ID: 68bbbd73ef5b
Revises: 
Create Date: 2024-10-06 18:59:34.129070

"""
from alembic import op
import sqlalchemy as sa
from core.server import db
from core.models.users import Users
from core.models.jobs import Jobs


# revision identifiers, used by Alembic.
revision = '68bbbd73ef5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('skills', sa.Text(), nullable=False),
                    sa.Column('experience_level', sa.Enum('JUNIOR', 'INTERMEDIATE', 'SENIOR', name='experiencelevelfield'), nullable=True)
    )
    
    op.create_table('jobs',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('title', sa.String(length=255), nullable=False),
                    sa.Column('skills', sa.Text(), nullable=False),
                    sa.Column('experience_level', sa.Enum('JUNIOR', 'INTERMEDIATE', 'SENIOR', name='experiencelevelfield'), nullable=True)
    )
    user_1 = Users(name='John Doe', skills='Python, Flask, SQLAlchemy', experience_level='SENIOR')
    db.session.add(user_1)
    db.session.flush()
    
    job_1 = Jobs(title='Python Developer', skills='Python, Flask, SQLAlchemy', experience_level='SENIOR')
    db.session.add(job_1)
    db.session.flush()
    
    db.session.commit()

def downgrade():
    pass
