# send message to all users

from twilio.rest import TwilioRestClient

from twilio_creds import twilio_account, twilio_token
from phone_numbers import phone_numbers


client = TwilioRestClient(account=twilio_account, token=twilio_token)

# phone_numbers = phone_numbers.phone_numbers


def send_sms_to_all(original_message):
    for name, phone in phone_numbers.iteritems():
        salutation = "Hello %s! " % (name.title())
        message = salutation + original_message
        print("sending the following message to %s at %s: %s" % (name, phone,  message))
        client.messages.create(
            # TODO: replace with\ messaging service SID later
            from_="(647) 560-9023",
            to=phone,
            body=message
        )


send_sms_to_all("If you hadn't already noticed, you haven't been getting quotes on your phone for quite a while now! Sorry about that-- it took a while to sort out some payment issues with Twilio, but we will be back to our regularly (randomly) scheduled programming starting today! Hope you've been enjoying the Project Roku beta otherwise :)")
