from flask import Flask, jsonify
import config
import requests

app = Flask(__name__)
GITHUB_TOKEN= "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"
ACCUKNOX_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1ODU2MTg5LCJqdGkiOiI2MDc5MzZmZGMwY2Y0ZWI1OGUwNzczYTc0ZDU0N2Y1MSIsImlzcyI6ImNzcG0uZGVtby5hY2N1a25veC5jb20ifQ.dD0WhHgZniKF1w0Y7QpmTcUySy3FG41RupI_4QAUnkqmG9tO1gOWZU8A0jp3qsDQ3Ah6lxfoNdgCThrD6kbLxeni2SFTKQxiSQMVJJMvNTtiDOH4e7lCff947C5swsdKVrT1mUBmS5oFGopAl5cew8t0v-5NG6jcoGnDWWsbIQr-GuF7EX55ACXIfpFL05sTe6PpAKt7CeYBwbxfkmlMAxmktQrmYfFTZAVtCGpjRLeKQvfzwSl_gAIVdNeSzKZp4jCmYj86AQjNu0G3kT27lB5CUnezWBvp40jVJiYiZ5IOkEv-ypAWiWIHNpA2hEmha1NyHERDoQuMPqyQQwkheg"
AWS_ACCESS_KEY_ID = "AWS23456789"
AWS_SECRET_ACCESS_KEY = "wJaSKJALKSKSJALKJSmamsals"

# GitHub PAT 
GITHUB_TOKEN = "git123456789"

# Slack Webhook (FAKE)
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/FAKEKEY123"

# Google API Key 
GOOGLE_API_KEY = "GoogleAPIKey123456789"

# Database Credentials 
DB_USER = "admin"
DB_PASSWORD = "123"

#Perplexity creds
PERPLEXITY_API_KEY="PERPANJHDJHncncsjsh1234"

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
