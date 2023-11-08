import os
import re
import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask import Flask, request, jsonify
# Code by AshishSecDev - Ashishsecdev@gmail.com
app = Flask(__name__)

SLACK_API_TOKEN = "XXXX" #User OAuth Token
os.environ['SLACK_API_TOKEN'] = SLACK_API_TOKEN
client = WebClient(token=os.environ['SLACK_API_TOKEN'])

def reply_with_notification(channel, ts, user):
    try:
        response = client.chat_postMessage(
            channel=channel,
            thread_ts=ts,
            text=f"<@{user}><Sensitive Information Shared - Message Removed>"
        )
        return response['ok']
    except Exception as e:
        print(f"Error replying to message: {e}")
        return False

def load_patterns_from_csv(file_path):
    patterns = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            patterns[row['pattern_name']] = row['pattern']
    return patterns

def find_matches(patterns, text):
    matches = {}
    for name, pattern in patterns.items():
        matches[name] = re.findall(pattern, text)
    return matches

def delete_message(channel, ts):
    try:
        response = client.chat_delete(channel=channel, ts=ts)
        return response['ok']
    except SlackApiError as e:
        print(f"Error deleting message: {e.response['error']}")
        return False

def save_to_csv(data):
    with open('violation-audit-report.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    if 'type' in data and data['type'] == 'url_verification':
        return jsonify({"challenge": data['challenge']})
    if 'event' in data and 'text' in data['event']:
        text = data['event']['text']
        user = data['event']['user']
        ts = data['event']['ts']
        message_time = data['event']['ts']


        patterns = load_patterns_from_csv('Slack_Guardian_Detections.csv')


        matches = find_matches(patterns, text)

        if any(matches.values()):
            channel = data['event']['channel']

            reply_text = f"<@{user}> <Sensitive Information Shared - Message Removed>."

            if reply_with_notification(channel, ts, user):
                delete_message(channel, ts)
                save_to_csv([user, channel, ts, message_time, text])
                return jsonify({"text": reply_text})
            else:
                return jsonify({"text": "Failed to send notification"})

    return jsonify({"text": ""})

if __name__ == '__main__':
    app.run(debug=True)
