from threading import Thread
import os
from replit import db
from time import sleep
from testejo import testa_page

db["al_disk"] = ""
db["al_tel"] = ""
db["disredaktu"] = ""


def vivu_telegram():
    os.system('python telegramo.py')


def vivu_discord():
    os.system('python diskordo.py')


def purigu_datumon():
  pass
   # os.system('python datumpurigilo.py')


def testejo_start():
    os.system('python testejo.py')


##Thread(target = vivu_telegram).start()
Thread(target=vivu_discord).start()
Thread(target=purigu_datumon).start()
Thread(target=testejo_start).start()

from flask import Flask, render_template
app = Flask(__name__, template_folder='')

@app.route('/')
def index():
  return render_template("retejo.html")

app.register_blueprint(testa_page)  
app.run(host='0.0.0.0', port=8080)