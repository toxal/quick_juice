import sys
import time
import telepot


"""
$ python3.5 skeletona.py <token>

A skeleton for your async telepot programs.
"""

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)

    chat_id = msg['chat']['id']
    command = msg['text']    
    bot.sendMessage(chat_id, "haha")


TOKEN = ""

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
