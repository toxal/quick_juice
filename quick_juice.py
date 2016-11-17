import os
import sys
import time
import telepot

configfile="~/.config/qj/qjconf.py"
sys.path.append(os.path.dirname(os.path.expanduser(configfile)))
import qjconf

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)

    chat_id = msg['chat']['id']
    command = msg['text']    
    bot.sendMessage(chat_id, "haha")



bot = telepot.Bot(qjconf.TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
