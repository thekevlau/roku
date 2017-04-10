from datetime import date, datetime
import calendar
import pytz

from twilio.rest import TwilioRestClient

from quotes import alex_quotes
import twilio_creds
import phone_numbers


client = TwilioRestClient(account=twilio_creds.twilio_account,
                          token=twilio_creds.twilio_token)

# note: cron job runs once per minute

# define timezone
eastern = pytz.timezone('US/Eastern')
# dummy timezone used for testing
# amsterdam = pytz.timezone('Europe/Amsterdam')

# get local copy of dictionary
alex_quotes = alex_quotes.alex_quotes

# Get today's day
today_day = calendar.day_name[date.today().weekday()]

# Get today's time, in specified timezone, put into format spec in dict
localized_time = datetime.now(eastern)
timestamp = localized_time.strftime('%H%M')

check_key = str(today_day + timestamp)

if (check_key in alex_quotes):
    print(alex_quotes[check_key])

    client.messages.create(
        from_="(647) 560-9023",
        to=phone_numbers["alex"],
        body=alex_quotes[check_key]
    )

    client.messages.create(
        from_="(647) 560-9023",
        to=phone_numbers["kevin"],
        body="Sent to Alex: " + alex_quotes[check_key]
    )
