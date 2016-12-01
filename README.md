## Project Roku

#### About
Effective personal management involves superb micro-control of doing every day tasks well, as well as a broad macro-perspective of one's goals, life purpose and ambitions.
Doing each of these things optimally requires intense focus and cognitive effort, and thus it is extremely difficult to maintain both states simultaneously in one's mind, especially over time.

In practice, most of our focus is spent on the immediate vagaries of every day life, on a very micro level.
Thus, many of the macro-level thoughts -- philosphical realizations, ideas about how to grow as an individual, theories about how to improve -- are forgotten, lost, and not implemented.

Project Roku is a service that remembers these thoughts for the indivudal and sends them regular text message reminders in order to keep them top-of-mind for the individual.

*This project is named for Avatar Roku, the wise mentor and advisor to Avatar Aang. Aang would often go to Roku for advice during times of distress or uncertainty.
However in the avatar universe, Aang is Roku's reincarnation, thus Roku is just helping Aang remember what he really already knows and realized in the past (from his previous life).*

---

#### Architecture

This service is currently just a python script, which randomly selects a quote (string) from a given list and sends them to a specific user's phone number using the Twilio API.
The pool of quotes randomly selected from differs based on the specific user's preferences.

---

#### Local Deployment

Activate the Python Virtual Environment for dependency/python package management:
```
source roku/bin/activate
```

Run the script :
**Be careful though, each time you run it, all our users get a round of text messages! If only testing, be sure to comment out the texting part of the code before running it!**
```
python send_sms.py
```

---

#### Contributing
Feel free to push directly to master **when editting your individual quote file**.
Otherwise, please submit pull requests so that I can review before merging. This is mainly for code-review and learning purposes.

I'm very interested in any good-programming-practice suggestions or product feedback or architectural design feedback you might have!
You are more than welcome to open an issue, submit a pull request or send me a message, any time!
