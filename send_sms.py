import random

from twilio.rest import TwilioRestClient

from quotes import avatar_quotes
from quotes import general_quotes
from quotes import kevin_quotes
from quotes import sandy_quotes
from quotes import andee_quotes
from twilio_creds import twilio_account, twilio_token
from phone_numbers import phone_numbers


client = TwilioRestClient(account=twilio_account, token=twilio_token)

# access local copies of dictionaries
avatar_quotes = avatar_quotes.avatar_quotes
general_quotes = general_quotes.general_quotes
kevin_quotes = kevin_quotes.kevin_quotes
sandy_quotes = sandy_quotes.sandy_quotes
andee_quotes = andee_quotes.andee_quotes

# send TWO messages between 7am and 7pm EST, so 12 hours or 720 minutes
# cron job runs once per minute,
for i in xrange(100000):
    if not (random.random() <= (1 / 36000000.0)):
        print("not this time")
        continue

    # randomly select message from public general quotes library
    selected_message = (random.choice(general_quotes))

    for k, v in phone_numbers.iteritems():
        random_message = selected_message
        if k == "kevin":
            # explicitly COPY the list, versus make a ref to it
            klau_messages = list(general_quotes)
            klau_messages.extend(kevin_quotes)
            random_message = (random.choice(klau_messages))
        # Alex has a different use case where he just wants avatar quotes
        # at a regular time in the mornings, so this functionality has been
        # Abstracted out into its own script now
        elif k == "alex":
            continue
        elif k == "shahmeer":
            # all messages plus avatar quotes
            # explicitly COPY the list, versus make a ref to it
            shahmeer_messages = list(general_quotes)
            shahmeer_messages.extend(avatar_quotes)
            random_message = (random.choice(shahmeer_messages))
        elif k == "andee":
            # all messages plus avatar quotes
            # explicitly COPY the list, versus make a ref to it
            andee_messages = list(general_quotes)
            andee_messages.extend(avatar_quotes)
            andee_messages.extend(andee_quotes)
            random_message = (random.choice(andee_messages))

        random_message = "Remember: " + random_message

        # sandy doesn't want the "remember" prefix
        # we have a separate script running for sandy already but he doesnt
        # mind getting more of them so we'll keep this in here for now
        if k == "sandy":
            random_message = (random.choice(sandy_quotes))

        print("sending the following message to %s at %s: %s" % (k, v, random_message))

        client.messages.create(
            # TODO: replace with\ messaging service SID later
            from_="(647) 560-9023",
            to=v,
            body=random_message
        )
