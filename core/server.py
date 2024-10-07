from core import app
from flask import jsonify, request
from core.logic import fetch_jobs

@app.route('/')
def ready():
    response = jsonify({
        'status': 'ready'
    })

    return response

@app.route('/recommend_jobs', methods=['GET', 'POST'])
def recommend_jobs():
    if request.method == 'POST':
        incoming_payload = request.get_json()
        if incoming_payload is None:
            return jsonify({"error": "Invalid payload"}), 400
        ranked_jobs = fetch_jobs.fetch_job_listings(incoming_payload)
        return jsonify({"message": "Successfully fetched matching jobs", "data": ranked_jobs}), 200
    return jsonify({"message": "Send a POST request with job recommendation data."}), 200