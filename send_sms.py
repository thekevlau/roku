import random

from twilio.rest import TwilioRestClient

from quotes import avatar_quotes
from quotes import general_motivational_quotes
from quotes import kevin_quotes
from quotes import sandy_quotes
import twilio_creds
import phone_numbers


client = TwilioRestClient(account=twilio_creds.twilio_account,
                          token=twilio_creds.twilio_token)

# get local copies of dictionaries
avatar_quotes = avatar_quotes.avatar_quotes
general_motivational_quotes = general_motivational_quotes.general_motivational_quotes
kevin_quotes = kevin_quotes.kevin_quotes
sandy_quotes = sandy_quotes.sandy_quotes

# get local copy of phone numbers dict, mapping username : phone number
phone_numbers = phone_numbers.phone_numbers

# send TWO messages between 7am and 7pm EST, so 12 hours or 720 minutes
# cron job runs once per minute,
for i in xrange(100000):
    if not (random.random() <= (1 / 36000000.0)):
        print("not this time")
        continue

    # randomly select message
    selected_message = (random.choice(general_motivational_quotes))

    for k, v in phone_numbers.iteritems():
        random_message = selected_message
        if k == "kevin":
            # explicitly COPY the list, versus make a ref to it
            klau_messages = list(general_motivational_quotes)
            klau_messages.extend(kevin_quotes)
            klau_messages.extend(avatar_quotes)
            random_message = (random.choice(klau_messages))
        # Alex has a different use case where he just wants avatar quotes
        # at a regular time in the mornings, so this functionality has been
        # Abstracted out into its own script now
        elif k == "alex":
            continue
        elif k == "shahmeer":
            # all messages plus avatar quotes
            # explicitly COPY the list, versus make a ref to it
            shahmeer_messages = list(general_motivational_quotes)
            shahmeer_messages.extend(avatar_quotes)
            random_message = (random.choice(shahmeer_messages))

        random_message = "Remember: " + random_message

        # sandy doesn't want the "remember" prefix
        if k == "sandy":
            random_message = (random.choice(sandy_quotes))

        print("sending the following message to %s at %s: %s" % (k, v, random_message))

        client.messages.create(
            # TODO: replace with\ messaging service SID later
            from_="(647) 560-9023",
            to=v,
            body=random_message
        )
