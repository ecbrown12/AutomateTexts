# code to automate text messages

# step 1: Pre made texts
gMorningQuotes = [
    "Good Morning Isabella!",
    "Good Morning, Hope you slept well.",
    "Good Morning babe, I love you!",
    "Hey, Have a nice day babe!"
]



# step 2: send the messages using Twilio API
from twilio.rest import Client
import schedule
import random

cellphone = 4193446233
twilio_number = 12533002821

def sendMessage(quote):
    account = "ACb7a0cbdc4ab315481cc4b5bd48ba3837"
    token = "a126b89fe223731666e6ef721127f63b"
    client = Client(account,token)

    client.messages.create(to=cellphone, from=twilio_number, body=quote)

# step 3: Schedule the texts messages 
quote = gMorningQuotes[random.randint(0, len(gMorningQuotes))]
schedule.every().day.at(6:00).do(sendMessage,quote)
