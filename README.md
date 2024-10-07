# Job Recommendation System

This project is a Flask-based job recommendation service that matches user profiles with suitable job listings based on skills, experience level, and preferences.

## Features

- RESTful API for job recommendations
- User profile validation
- Job listing ranking based on skill match
- Database integration with SQLAlchemy
- Alembic migrations for database schema management

## Project Structure

- `core/server.py`: Main Flask application with API routes
- `core/logic/rank_jobs.py`: Job listing fetching and ranking logic
- `core/logic/payload_validation.py`: User profile validation
- `core/migrations/`: Database migration scripts
- `core/models/`: SQLAlchemy models for database tables

## Setup and Running

```
git clone https://github.com/parulhardaha/job-recommendation-system.git
cd job-recommendation-system

pip install -r requirements.txt
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
flask run

```

## Sample API
### Request
```
curl --location 'http://127.0.0.1:5000/recommend_jobs' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Jane Doe",
    "skills": [
        "Python",
        "Java",
        "Hibernate"
    ],
    "experience_level": "Senior",
    "preferences": {
        "desired_roles": [
            "Python Developer",
            "Software Engineer"
        ],
        "locations": [
            "Remote",
            "New York"
        ],
        "job_type": "Full-Time"
    }
}'
```
### Response
```
{
    "data": [
        {
            "company": "123 Tech",
            "experience_level": "Senior",
            "job_type": "Full-Time",
            "location": "Remote",
            "required_skills": [
                "Java",
                "Spring",
                "Hibernate"
            ],
            "skill_match_score": 0.67,
            "title": "Software Engineer"
        },
        {
            "company": "ABC Corp",
            "experience_level": "Senior",
            "job_type": "Full-Time",
            "location": "New York",
            "required_skills": [
                "Python",
                "Flask",
                "SQLAlchemy"
            ],
            "skill_match_score": 0.33,
            "title": "Python Developer"
        }
    ],
    "message": "Successfully fetched matching jobs"
}
```

## Internal Job Ranking Logic

* The heuristic algorithm primarily uses set operations to calculate how well the user's skills match the required skills for each job.
* The jobs are then ranked by the percentage of skills matched, in descending order.
* The matching for experience_level, job_type, location, and job_title happens in the SQL query, so the skills matching is done in the Python code

## Detailed doc
https://docs.google.com/document/d/1ukV2l8GKIeookZxQsqzJr1QKatwwxqJaj6vKqXddyqg/edit
