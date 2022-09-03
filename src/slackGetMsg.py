import datetime
import requests
import settings
import pandas as pd

SLACK_CHANNEL_ID = settings.SLACK_CHANNEL_ID
SLACK_URL = settings.SLACK_URL
TOKEN = settings.TOKEN


def main():

    payload = {
        "channel": SLACK_CHANNEL_ID,
        "limit": "1000"
    }
    headersAuth = {
        'Authorization': 'Bearer ' + str(TOKEN),
    }
    response = requests.get(SLACK_URL, headers=headersAuth, params=payload)
    json_data = response.json()
    msgs = json_data['messages']

    text_list = []
    time_list = []
    list = []
    for msg in msgs:
        try:
            text = msg["text"]
            ts = float(msg["ts"])
            text_list.append(text)
            dt = datetime.datetime.fromtimestamp(ts)
            s = dt.strftime("%Y-%m-%d %H:%M:%S")
            time_list.append(s)
            list.append([text, s])
        except KeyError:
            pass

    df = pd.DataFrame(list, columns=['テキスト', '日付'])
    df.to_excel('xxxxx.xlsx')
    print(df)

    return


if __name__ == "__main__":
    main()
