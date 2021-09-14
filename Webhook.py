import requests
import os
from os import system
import platform

if platform.system == ("linux"):
    os.system("clear")
else:
    os.system("cls")

print('Simple Discord webhook sender in Python\n')
a = input('Enter Webhook : ')
b = input('Enter Avatar : ')
c = input('Enter Username: ')

def webhook():
    while True:
        try:
            webhook = (a)
            avatar = (b)
            username = (c)
            message = input("Enter Message : ")
            data = requests.post(webhook, json={'content': message, 'avatar_url': avatar, "username": username})

            if data.status_code == 204:
                print('\n' 'Sent : ' + message)
                print('To : ' + a, '\n')
            else:
                print("\nWebhook Error Deleted\n-> " + webhook)
                break
        except:
            break

webhook()
