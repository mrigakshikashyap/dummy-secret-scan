from flask import Flask, jsonify
import config
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Dummy App"}), 200

@app.route("/send-alert")
def send_alert():
    message = {"text": "This is a test alert from Leaky Dummy App."}
    response = requests.post(config.SLACK_WEBHOOK, json=message)
    return jsonify({"status": response.status_code}), response.status_code

@app.route("/repos")
def list_github_repos():
    headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)
    return jsonify({"status": response.status_code}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
