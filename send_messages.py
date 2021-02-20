import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_message(groupme_bot, form_link, msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get(DAILY_RPE_BOT),
        'text': "{} {}".format(msg, RPE_link),
    }
    tries = 3
    for i in range(tries):
        try:
            print("sending to bot {}".format(groupme_bot))
            request = Request(url, urlencode(data).encode())
            json = urlopen(request).read().decode()
            print("success sending to bot {}".format(groupme_bot))
            print("response: {}".format(json))
            break
        except Exception as e:
            print("failed sending to bot {}".format(groupme_bot))
            print(e)

