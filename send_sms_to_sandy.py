# DEPRICATED
import random

from twilio.rest import TwilioRestClient

from quotes import sandy_quotes
from twilio_creds import twilio_account, twilio_token
from phone_numbers import phone_numbers


client = TwilioRestClient(account=twilio_account, token=twilio_token)

# get dictionary
sandy_quotes = sandy_quotes.sandy_quotes

# note: cron job runs once per minute
# send ~30 messages between 7am and 12pm PST, so 17 hours or 1020 minutes
for i in xrange(100000):
    if not (random.random() <= (1 / 3400000.0)):
        print("not this time")
        continue

    client.messages.create(
        from_="(647) 560-9023",
        to=phone_numbers["sandy"],
        body=sandy_quotes[0]
    )
