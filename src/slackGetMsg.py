import requests
import settings

SLACK_CHANNEL_ID = settings.SLACK_CHANNEL_ID
SLACK_URL = settings.SLACK_URL
TOKEN = settings.TOKEN

def main():

    payload = {
        "channel": SLACK_CHANNEL_ID,
        "oldest": "1622761200"
    }
    headersAuth = {
    'Authorization': 'Bearer '+ str(TOKEN),
    }  
    response = requests.get(SLACK_URL, headers=headersAuth, params=payload)
    json_data = response.json()
    msgs = json_data['messages']
    for msg in msgs:
        print(msg['text'])
    return 

if __name__ == "__main__":
    main()