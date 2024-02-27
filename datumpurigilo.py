from replit import db
from threading import Thread
import time 

print("Datumpurigilo estas ŝaltita")  

def datumbazaj_komandoj():
  while True:
    a = input()
    if a == "kio":
      print(db.keys())
      a = 0

def purigilo():
  while True:
    for letero in db:
      if letero != "al_disk" and letero != "al_tel" and letero != "disredaktu"and letero != "telredaktu":        
        if float(letero) + (27*3600) < time.time():
          del db[letero]        
    time.sleep(10)  

Thread(target = datumbazaj_komandoj).start()
Thread(target = purigilo).start()
  