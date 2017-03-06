import random

from twilio.rest import TwilioRestClient

from quotes import avatar_quotes
import twilio_creds
import phone_numbers


client = TwilioRestClient(account=twilio_creds.twilio_account,
                          token=twilio_creds.twilio_token)

# send one msg between hours of 8am and 12pm, so 4 hours or 240 minutes
# cron job runs once per minute,
for i in xrange(100000):
    if not (random.random() <= (1 / 24000000.0)):
        print("not this time")
        continue

    # get local copies of dictionaries
    avatar_quotes = avatar_quotes.avatar_quotes

    # get local copy of phone numbers dict, mapping username : phone number
    phone_numbers = phone_numbers.phone_numbers

    # randomly select message
    random_message = (random.choice(avatar_quotes))

    print("sending the following message to alex at %s: %s" % (phone_numbers["alex"], random_message))

    client.messages.create(
        from_="(647) 560-9023",
        to=phone_numbers["alex"],
        body=random_message
    )

    print("sending the following message to kevin at %s: %s" % (phone_numbers["kevin"], random_message))

    client.messages.create(
        from_="(647) 560-9023",
        to=phone_numbers["kevin"],
        body=random_message
    )
