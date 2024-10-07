"""
Validates the user profile data to ensure it meets the required structure and constraints.

Args:
    user_profile (dict): A dictionary containing the user's profile data.

Returns:
    None if all validations pass, otherwise a Flask JSON response with an error message and HTTP status code 400.
"""
from flask import jsonify
from core.constants import constant


def validate_user_profile(user_profile):
    # Validate the presence of required fields
    required_fields = ['skills', 'experience_level', 'preferences']
    for field in required_fields:
        if field not in user_profile:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate preferences structure
    preferences = user_profile['preferences']
    required_preferences = ['desired_roles', 'locations', 'job_type']
    for field in required_preferences:
        if field not in preferences:
            return jsonify({"error": f"Missing required preference field: {field}"}), 400

    # Validate skills
    if not isinstance(user_profile['skills'], list) or not user_profile['skills']:
        return jsonify({"error": "Invalid or missing skills. It should be a non-empty list."}), 400

    # Validate experience level
    if constant.ExperienceLevelMapping[user_profile['experience_level']] not in constant.ExperienceLevelEnum.__members__:
        return jsonify({"error": f"Invalid experience level. It should be one of: {', '.join(constant.ExperienceLevelEnum.__members__)}."}), 400

    # Validate desired roles
    if not isinstance(preferences['desired_roles'], list) or not preferences['desired_roles']:
        return jsonify({"error": "Invalid or missing desired roles. It should be a non-empty list."}), 400

    # Validate locations
    if not isinstance(preferences['locations'], list) or not preferences['locations']:
        return jsonify({"error": "Invalid or missing locations. It should be a non-empty list."}), 400

    # Validate job type
    if constant.JobTypeMapping[preferences['job_type']] not in constant.JobTypeEnum.__members__:
        return jsonify({"error": f"Invalid job type. It should be one of: {', '.join(constant.JobTypeEnum.__members__)}."}), 400

    return None  # Return None if all validations pass
