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
b = input('Enter Avatar [url] : ')
c = input('Enter Username : ')

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
                continue
            else:
                data = requests.post(webhook, json={'content': message, "username": username})
                if data.status_code == 204:
                 print('\n' 'Sent : ' + message)
                 print('To : ' + a, '\n')
                 continue
                else:
                    print("\nWebhook Error or Deleted!\n-> " + webhook)
                    break
            print("\nWebhook Error or Deleted!\n-> " + webhook)
        except:
            print('\nSomething happend! / cannot connect to the webhook.')
            break

webhook()
