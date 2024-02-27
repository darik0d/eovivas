from telebot.async_telebot import AsyncTeleBot
from telebot import util, types
from threading import Thread
from replit import db
import asyncio
import time

import os

T_TOKEN = os.environ['T_TOKEN']

bot = AsyncTeleBot(T_TOKEN)

async def dormu(a):
  time.sleep(a)
@bot.edited_message_handler()


async def redaktu(message):
  print(message.from_user.first_name, "redaktis al", message.text, "idilo:", message.id)
  for a in db:
    if db[a]["idilo"] == message.id:
      print("Mi trovis redaktitan telegraman mesaĝon ")
      db["disredaktu"] = db[a]
      db["disredaktu"]["letero"] = message.text
      del db[a]
  
  
  
@bot.message_handler(content_types = ['text', "voice", "document", "audio"])
async def echo(message):
  print("telegramo vidas")
  if message.text:
    letero = message.text
    autoro = message.from_user.first_name
    print(letero)
    print(autoro)
    tempo = time.time()
    if message.reply_to_message:
      db["al_disk"] = {"aŭtoro": autoro, "letero": letero, "idilo": message.id, "tempo": tempo, "respondita": {"aŭtoro": message.reply_to_message.from_user.first_name, "letero": message.reply_to_message.text, "idilo": message.reply_to_message.id}}
    else:
      db["al_disk"] = {"aŭtoro": autoro, "letero": letero, "idilo": message.id, "tempo": tempo, "respondita": {"aŭtoro": None, "letero": None, "idilo": None}}
  else:
    print("io alia")

async def sendu_al_tel(): 
 print("la roboto aŭskultas al_tel datumaron") 
 while True: 
  if db["al_tel"] != "":
    tempo = time.time()
    print("Al telegramo: ", db["al_tel"]["aŭtoro"], ": " , db["al_tel"]["letero"])
    db[tempo] = db["al_tel"]
    db["al_tel"] = ""
  await dormu(0.1)    

def interfunkcio():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sendu_al_tel())
    loop.close()

if __name__ == '__main__':
  #async def komenco_tel():
    print("nura name teleg funkc")
    Thread(target = interfunkcio).start()
    print("telegrama roboto estos ŝaltita")  
    asyncio.run(bot.infinity_polling(allowed_updates=util.update_types))
  #komenco_tel() 

