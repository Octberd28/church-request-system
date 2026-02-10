from flask import Flask, request, jsonify

app = Flask(__name__)

requests_db = []


@app.route("/requests", methods=["POST"])
def add_request():
    data = request.json
    data["status"] = "Pending"
    requests_db.append(data)
    return jsonify({"message": "Request added"})


@app.route("/requests", methods=["GET"])
def get_requests():
    return jsonify(requests_db)


@app.route("/requests/<int:index>", methods=["PUT"])
def update_request(index):
    if index < 0 or index >= len(requests_db):
        return jsonify({"error": "Invalid request index"}), 404

    decision = request.json.get("status")
    requests_db[index]["status"] = decision
    return jsonify({"message": "Updated"})


if __name__ == "__main__":
    app.run(port=5001)
