import json, os
from DataStructures import Queue
from sms import send

from twilio.rest import Client
if os.getenv("account_sid") is None or os.getenv("account_sid") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token)

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(person):
    queue.enqueue(person)
    print(queue._queue)

def dequeue():
    queue.dequeue()
    print(queue._queue)
    message = client.messages.create(
    to=queue.popped, 
    from_="+15017250604",
    body="Hello from Python!")
    print(message.sid)

def save():
    with open("queue.json", "w") as f:
        json.dump(queue._queue, f)

def load():
    with open("queue.json", "r") as f:
        content = f.readlines()
        print(content)
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    elif option == 1:
        add(input("What is your phone number?"))
    elif option == 2:
        dequeue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    else:
        print("Not implemented yet or invalid option "+str(option))
