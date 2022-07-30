from requests import post, get
import random, string, threading, os
from datetime import datetime
import time
from pystyle import Colors, Colorate

os.system("cls")
print(Colorate.Horizontal(Colors.rainbow,"""
    ╔═══╗╔╗   ╔╗ ╔╗╔═══╗╔═╗╔═╗╔═══╗╔══╗╔════╗╔═══╗
    ║╔═╗║║║   ║║ ║║║╔══╝║║╚╝║║║╔═╗║╚╣╠╝╚══╗ ║║╔══╝
    ║╚═╝║║║   ║║ ║║║╚══╗║╔╗╔╗║║╚══╗ ║║   ╔╝╔╝║╚══╗
    ║╔══╝║║ ╔╗║║ ║║║╔══╝║║║║║║╚══╗║ ║║  ╔╝╔╝ ║╔══╝
    ║║   ║╚═╝║║╚═╝║║╚══╗║║║║║║║╚═╝║╔╣╠╗╔╝ ╚═╗║╚══╗
    ╚╝   ╚═══╝╚═══╝╚═══╝╚╝╚╝╚╝╚═══╝╚══╝╚════╝╚═══╝            (PLUEMSIZE#9007)                                              
"""))
webhook = input("webhook_url: ")
r = input('amount: ')
username = input('username: ')
content = input("content: ")
    
def send(timestampStr, avatars):
    
    json = {"content": content, "username": f"{username} | "+''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=4)), "avatar_url": avatars}

    r = post(webhook, json=json)
    if (send):
        print(Colorate.Horizontal(Colors.red_to_blue, f'[{timestampStr}] send webhook  or content {content}'))
    else:
        print(f"\x1b[38;5;21m[{timestampStr}] \x1b[0mrate Limit {r.json()['retry_after']}")
    
def run_send():
    avatar = open('avatar.txt', 'r')
    channel = []
    for avatars in avatar or range(int(r)):
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%H:%M:%S")
        t = threading.Thread(target=send, args=(timestampStr, avatars))
        t.start()
        channel.append(t)
    for channels in channel:
        channels.join()
    time.sleep(3)
    input(f"\x1b[38;5;21m[{timestampStr}] \x1b[0msend amount {r}")

run_send()