import discord
import os
from replit import db
from threading import Thread
import asyncio
import time

D_TOKEN = os.environ['D_TOKEN']

if __name__ == '__main__':
  client = discord.Client()
  print("unua name disk funkc")  
else:
  print(__name__)

async def dormu(a):
  time.sleep(a)

@client.event
async def on_message(message):
 print("diskordo vidas!")
 if message.channel.id == 939675444335239329:
   if message.content:
      letero = message.content
      autoro = message.author.display_name
      print(letero)
      print(autoro)
      tempo = time.time()
      if message.reference:
        respondita = await message.channel.fetch_message(message.reference.message_id)
        db["al_tel"] = {"aŭtoro": autoro, "letero": letero, "idilo": message.id, "tempo": tempo, "respondita": {"aŭtoro": respondita.author.display_name,"letero": respondita.content, "idilo": message.reference.message_id}}
      else:
        db["al_tel"] = {"aŭtoro": autoro, "letero": letero, "idilo": message.id, "tempo": tempo, "respondita": {"aŭtoro": None, "letero": None, "idilo": None}}

@client.event
async def on_ready():
  print(f'{client.user} estas konektita!')
 # forigu komenton por ponta roboto
  """
async def sendu_al_disk():
  while True:
    if db["al_disk"] != "":
      print("Al diskordo: ", db["al_disk"]["aŭtoro"], ": " , db["al_disk"]["letero"])
      #tempo = time.time()
      db[db["al_disk"]['tempo']] = db["al_disk"]
      kanalo = client.get_channel(939675444335239329)
      print(f"Ricevis {kanalo}")
      await kanalo.send(f"_{str(db[db['al_disk']['tempo']]['aŭtoro'])}_: <br />")
      await kanalo.send(f"{str(db[db['al_disk']['tempo']]['letero'])}")
      db["al_disk"] = ""
    if db["disredaktu"] != "":
      print("Mi redaktis diskordan mesaĝon!")
      db[db["disredaktu"]["tempo"]] = db["disredaktu"]
      db["disredaktu"] = ""
      print("Kaj nun ĝi eĉ estas en la datumbazo!")
      
    await dormu(0.1)
    
def interfunkcio():
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(sendu_al_disk())
  loop.close()

#async def atendu_al_disk(): 
Thread(target = interfunkcio).start() 
"""
client.run(D_TOKEN) 
   
      #kanalo = client.get_channel(939675444335239329)
      #kanalo.send(k.readlines())




