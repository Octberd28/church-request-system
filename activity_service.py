from flask import Flask, request, jsonify

app = Flask(__name__)

activity_log = []

@app.route("/log", methods=["POST"])
def add_log():
    activity_log.append(request.json["message"])
    return jsonify({"message": "Logged"})


@app.route("/log", methods=["GET"])
def get_log():
    return jsonify(activity_log)


if __name__ == "__main__":
    app.run(port=5002)
