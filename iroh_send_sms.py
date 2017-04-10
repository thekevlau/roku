# Modified version of send_sms.py for SYDE 322
# Connects to a (local) MySQL database for phone numbers, names and quotes

from collections import defaultdict
import random

from twilio.rest import TwilioRestClient
import mysql.connector

import twilio_creds


client = TwilioRestClient(account=twilio_creds.twilio_account,
                          token=twilio_creds.twilio_token)

# connect to database
try:
    conn = mysql.connector.connect(
        host='localhost',
        database='iroh',
        user='root',
        password='helloworld'
    )

    if conn.is_connected():
        print('Connected to MySQL database')
    else:
        print('no go!')

    user_query = "SELECT username FROM user"
    cursor = conn.cursor()
    cursor.execute(user_query)
    username_list = list()
    for username in cursor:
        username_list.append(str(username[0]))

    conn.commit()

except mysql.connector.Error as e:
    print ("uhoh")
    print(e)

finally:
    conn.close()

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='iroh',
        user='root',
        password='helloworld'
    )

    if conn.is_connected():
        print('Connected to MySQL database')
    else:
        print('no go!')

    user_quote_dd = defaultdict(dict)
    for user in username_list:
        quote_query = "SELECT quote_text, phone_number FROM quote INNER JOIN user ON submitter_user_id = user_id WHERE username = '%s'" % (user)
        cursor = conn.cursor()
        cursor.execute(quote_query)
        user_quote_dd[user]['quotes'] = list()
        for quote in cursor:
            user_quote_dd[user]['quotes'].append(str(quote[0]))
            user_quote_dd[user]['phone_number'] = str(quote[1])

    conn.commit()

except mysql.connector.Error as e:
    print ("uhoh")
    print(e)

finally:
    conn.close()

user_quote = dict(user_quote_dd)
print(user_quote)

# send TWO messages between 7am and 7pm EST, so 12 hours or 720 minutes
# cron job runs once per minute,

# randomly select message
for k, v in user_quote.iteritems():
    random_message = (random.choice(v['quotes']))

    print("sending the following message to %s at %s: %s" % (k, v['phone_number'], random_message))

    client.messages.create(
        # TODO: replace with\ messaging service SID later
        from_="(647) 560-9023",
        to=v['phone_number'],
        body=random_message
    )
