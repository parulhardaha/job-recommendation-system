"""
Fetches and ranks job listings based on a user's profile and skills.

The `fetch_job_listings` function takes a user profile dictionary as input and returns a list of ranked job listings. It first retrieves the job listings from the database based on the user's skills, experience level, desired roles, locations, and job type. It then formats the job listings and ranks them based on the user's skills.

The `format_job_profile` function takes a job profile object and returns a dictionary with the relevant job information, such as title, company, required skills, experience level, location, and job type.

The `calculate_skill_match` function takes a list of user skills and a list of required skills for a job, and calculates the percentage of matching skills.

The `rank_job_listings` function takes a list of formatted job listings and the user's skills, and returns a list of job listings sorted by the skill match score in descending order.
"""
from core.models.jobs import Jobs
from core.constants import constant
import json


def fetch_job_listings(user_profile):

    try:
        job_listings = Jobs.get_jobs(
            _skills=user_profile['skills'],
            _experience_level=constant.ExperienceLevelMapping[user_profile['experience_level']],
            _desired_roles=user_profile['preferences']['desired_roles'],
            _locations=user_profile['preferences']['locations'],
            _job_type=constant.JobTypeMapping[user_profile['preferences']['job_type']]
        )

        if not job_listings:
            return []

        formatted_job_listings = [
            format_job_profile(job) for job in job_listings]

        return rank_job_listings(formatted_job_listings, user_profile['skills'])

    except KeyError as e:
        return {"error": f"Invalid user profile key: {str(e)}"}, 400
    except Exception as e:
        return {"error": f"An error occurred while fetching job listings: {str(e)}"}, 500


def format_job_profile(job_profile):
    try:
        return {
            'title': job_profile.title,
            'company': job_profile.company,
            'required_skills': json.loads(job_profile.required_skills),
            'experience_level': job_profile.experience_level,
            'location': job_profile.location,
            'job_type': job_profile.job_type
        }
    except json.JSONDecodeError:
        return {"error": "Error decoding job skills JSON."}, 500

def calculate_skill_match(user_skills, required_skills):
    # Convert to sets for easier comparison
    user_skills_set = set(user_skills)
    required_skills_set = set(required_skills)

    # Find the number of matching skills
    matching_skills = user_skills_set.intersection(required_skills_set)

    # Calculate match percentage
    if len(required_skills_set) == 0:
        return 0

    match_percentage = len(matching_skills) / len(required_skills_set)

    return match_percentage


def rank_job_listings(job_list, user_skills):
    recommended_jobs = []

    for job in job_list:
        
        print("hshsh", job['required_skills'], type(job['required_skills']))
            # Calculate the skill match percentage
        skill_match = calculate_skill_match(
            user_skills, job['required_skills'])

        # Add the job and its match score to the recommendations
        job_with_score = job.copy()
        job_with_score['skill_match_score'] = skill_match
        recommended_jobs.append(job_with_score)

    # Sort jobs by skill match score (highest first)
    recommended_jobs.sort(key=lambda x: x['skill_match_score'], reverse=True)

    return recommended_jobs
