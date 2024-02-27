print("Vere, la testejo estas lanĉita...")
import telebot
import discord
import time
import os
from threading import Thread
from flask import Flask, render_template
from decouple import config

app = Flask(__name__, template_folder='')

# Use nested dictionaries instead of replit.db
retbazo = {}
retteksto = {"content": "", "counter": 0}

print("Paŝo 1")

def purigilo():
    nombro = 0
    komenc = -1
    cento = -1
    print(retteksto["content"][retteksto["content"].rfind("<arti"):])
    while True:
        komenc = retteksto["content"].find("<article", komenc + 1)
        if komenc == -1:
            break
        nombro += 1
        if nombro == 101:
            cento = komenc
            print("komenc = ", komenc)
    print(nombro)
    if nombro > 100 and cento != -1:
        retteksto["content"] = retteksto["content"][:cento]
        print("Mi sukcese purigis")
    elif nombro > 100 and cento == -1:
        print("Nombro > 100, sed cento = -1")
    else:
        print("Mi devas nenion purigi")

@app.route('/')
def index():
    return render_template("retlisto.html", montrajo=retteksto["content"])

T_TOKEN = config('testat_token')
D_TOKEN = config('d_token')
bot = telebot.TeleBot(T_TOKEN)

@bot.message_handler(content_types=['text'])
def show(message):
    print("Mi ekvidis")
    print(message.text)
    retbazo[str(int(time.time()))] = ['telegramo', 'Nova mesaĝo ĉe telegramo!']
    piktogramo = ''
    teksto_ago = ''
    minutes = lambda: "0" + str(time.gmtime().tm_min) if len(str(time.gmtime().tm_min)) == 1 else str(time.gmtime().tm_min)
    nova_tekst = '''<article class="lasta_ago">
      <img src="/static/tlg_logo.webp" alt="Telegramo" class="aga_bildo">
      <span class="aga_teksto">Nova mesaĝo ĉe telegramo!</span>
      <span class="tempo">'''
    nova_teskt = nova_tekst + str(time.gmtime().tm_hour) + ':' + str(minutes()) + '</span>' + '</article>'
    retteksto["content"] = nova_teskt + retteksto["content"]
    print("konservis tekston")
    purigilo()

def interfunkcio():
    bot.remove_webhook()

def lancu_retejon():
    app.run(host='0.0.0.0', port=8080)

def komandoj():
    while True:
        a = input()
        if a == "prg":
            retteksto["content"] = ""
            print("retteksto purigita")
        elif a == "retteksto":
            print(retteksto["content"])
        elif a == "db":
            for i in retbazo:
                print(i)
        elif a == "100":
            nombro = 0
            komenc = -1
            cento = -1
            print(retteksto["content"][retteksto["content"].rfind("<arti"):])
            while True:
                komenc = retteksto["content"].find("<article", komenc + 1)
                if komenc == -1:
                    break
                nombro += 1
                if nombro == 101:
                    cento = komenc
                    print("komenc = ", komenc)
            print(nombro)
            if nombro > 100 and cento != -1:
                retteksto["content"] = retteksto["content"][:cento]
                print("Mi sukcese purigis")
            elif nombro > 100 and cento == -1:
                print("Nombro > 100, sed cento = -1")
            else:
                print("Mi devas nenion purigi")

def diskordajoj():
    client = discord.Client(intents=discord.Intents.default())
    @client.event
    async def on_ready():
        print(f'{client.user} estas konektita!')
    @client.event
    async def on_message(message):
        print("Nova diskorda mesaĝo!")
        retbazo[str(int(time.time()))] = ['diskordo', 'Nova mesaĝo ĉe diskordo!']
        piktogramo = ''
        teksto_ago = ''
        minutes = lambda: "0" + str(time.gmtime().tm_min) if len(str(time.gmtime().tm_min)) == 1 else str(time.gmtime().tm_min)
        nova_tekst = '''<article class="lasta_ago">
          <img src="/static/dsk_logo.png" alt="Diskordo" class="aga_bildo">
          <span class="aga_teksto">Nova mesaĝo ĉe diskordo!</span>
          <span class="tempo">'''
        nova_teskt = nova_tekst + str(time.gmtime().tm_hour) + ':' + str(minutes()) + '</span>' + '</article>'
        retteksto["content"] = nova_teskt + retteksto["content"]
        print("konservis tekston")
        purigilo()

    client.run(D_TOKEN)

if __name__ == '__main__':
    Thread(target=lancu_retejon).start()
    Thread(target=komandoj).start()
    print("retejo k komandoj ŝaltitaj")
    Thread(target=diskordajoj).start()
    bot.infinity_polling()


###############################
"""
from pyrogram import Client, filters
import os
from time import sleep
from pyrogram.errors import FloodWait

print("Testejo lanĉita")

api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
app = Client("my_account", api_id, api_hash)


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = " ...✍️"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


@app.on_deleted_messages(filters.chat("Esperantujoo"))
async def forigtrovilo(client, message):
    print("Mesaĝo estis forigita")
    print(message.text)


@app.on_raw_update()
async def raw(client, update, users, chats):
    print("Ĝisdatigo!")
    print(update)
"""