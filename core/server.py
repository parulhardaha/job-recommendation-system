"""
Provides the main Flask application routes for the job recommendation service.

The `ready()` function returns a JSON response indicating that the service is ready to receive requests.

The `recommend_jobs()` function handles POST requests to the `/recommend_jobs` endpoint. It validates the incoming payload, fetches the ranked job listings based on the user profile, and returns a JSON response with the matching jobs or an error message.
"""
from core import app
from flask import jsonify, request
from core.logic import rank_jobs, payload_validation

@app.route('/')
def ready():
    response = jsonify({
        'status': 'ready'
    })

    return response

@app.route('/recommend_jobs', methods=['POST'])
def recommend_jobs():
    if request.method == 'POST':
        try:
            incoming_payload = request.get_json()
            if incoming_payload is None:
                return jsonify({"error": "Invalid payload: JSON body required"}), 400

            # Validate user profile
            validation_error = payload_validation.validate_user_profile(
                incoming_payload)
            if validation_error:
                return validation_error

            ranked_jobs = rank_jobs.fetch_job_listings(incoming_payload)
            
            # Check if the ranked job list is empty
            if not ranked_jobs:
                return jsonify({"message": "No matching jobs found for the provided profile."}), 404
            
            return jsonify({"message": "Successfully fetched matching jobs", "data": ranked_jobs}), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"message": "Send a POST request with job recommendation data."}), 200
