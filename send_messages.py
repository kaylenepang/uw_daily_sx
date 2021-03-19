import json
import os
import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_message(groupme_bot, form_link, msg):
    url = 'https://api.groupme.com/v3/bots/post'
    bot_id = os.environ.get(groupme_bot)
    message_text = "{} {}".format(msg, form_link)
    url_with_params = "{}?bot_id={}&text={}".format(url, bot_id, message_text)

    print("sending to bot {}".format(groupme_bot))
    tries = 4
    for i in range(tries):
        try:
            # request = Request(url, urlencode(data).encode())
            # json = urlopen(request).read().decode()
            response = requests.post(url_with_params)
            if response.ok:
                print("success sending to bot {} on try number {}".format(groupme_bot, i + 1))
                break
            print("failed: {}".format(response.text))
        except Exception as e:
            print("failed for bot {} on try number {} - error: {}".format(groupme_bot, i + 1, e))
