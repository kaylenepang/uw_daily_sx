import os
from datetime import date
from send_messages import send_message
from constants import RPE_MESSAGE

# Messages to be sent only on specific days should be in an if-statement like below:
# Messages to be sent only on Thursdays
# if date.today().weekday() == 3:
#     send_message(
#         'FOOTBALL_q', 'FB_Q_DAILY', RPE_MESSAGE
#     )

# Days:
# 0- Monday
# 1- Tuesday
# 2- Wednesday
# 3- Thursday
# 4- Friday
# 5- Saturday
# 6- Sunday


# DAILY FOOTBALL MESSAGE TO QUARANTINED ATHLETES
send_message(
    'DAILY_RPE_BOT', # players text bot from heroku configs
    os.environ.get('RPE_LINK'), # google form link from heroku configs
    RPE_MESSAGE # message
)

import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_message(groupme_bot, form_link, msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get(groupme_bot),
        'text': "{} {}".format(msg, form_link),
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
