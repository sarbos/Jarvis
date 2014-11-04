from twilio.rest import TwilioRestClient
import sys
#read RFID stuff here

received = sys.argv[1]
account_sid = sys.argv[2]
auth_token = sys.argv[3]
client = TwilioRestClient(account_sid, auth_token)
#twilio_num = sys.argv[4]
roommates = ["JO", "JD", "SS"]
numbers = ["8134282970","8134282970","8134282970"]
text = ""
person = received[:2]
task = received[3:]
if task == "dishes":
  text = "Did " + person + " do the dishes?"
elif task == "trash":
  text = "Did " + person + " take out the trash?"
send_to = []
for p, n in zip(roommates, numbers):
  if p != person:
    send_to.append(n)
for n in send_to:
  message = client.messages.create(body=text, to="+1" + n, from_="+18137937914")

