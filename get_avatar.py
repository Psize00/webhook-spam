from requests import get
import os, threading

def get_avatar():
    try:
        os.remove("avatar.txt")
    except: pass
    with open('avatar.txt', 'a') as w:
        api = 'https://api.waifu.pics/nsfw/waifu'
        req_url = get(api)
        url = req_url.json()['url']
        print(url)
        w.write(str(url) + "\n")
    w.close()
    
def speed_get_avatar():
    for i in range(int(500)):
        threading.Thread(target=get_avatar).start()
    
speed_get_avatar()