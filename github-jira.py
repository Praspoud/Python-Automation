import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os
from flask import Flask

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def create_jira():
  url = "https://prasispoudel1-1735224107566.atlassian.net/rest/api/3/issue"

  load_dotenv()
  API_TOKEN = os.getenv("API_TOKEN")
  auth = HTTPBasicAuth("prasispoudel1@gmail.com", API_TOKEN)

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  payload = json.dumps( {
    "fields": {
      "description": {
        "content": [
          {
            "content": [
              {
                "text": "My first jira ticket.",
                "type": "text"
              }
            ],
            "type": "paragraph"
          }
        ],
        "type": "doc",
        "version": 1
      },
      "issuetype": {
        "id": "10003"
      },
      "project": {
        "key": "SCRUM"
      },
      "summary": "First jira ticket.",
    },
    "update": {}
  } )

  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
  )

  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)