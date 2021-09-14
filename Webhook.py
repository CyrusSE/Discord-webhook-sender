import requests
import os
from os import system

os.system('cls')

a = input('Enter Webhook : ')

def webhook():
    while True:
        try:
            webhook = (a)
            message = input("Enter Message: ")
            data = requests.post(webhook, json={'content': message})

            if data.status_code == 204:
                print('\n' 'Sent : ' + message)
                print('To : ' + a, '\n')
            else:
                print("\nInvalid webhook or Deleted \n-> " + webhook)
                break
        except:
            break

webhook()