import requests
import time
import random
import os
from requests.structures import CaseInsensitiveDict


def notification(content, date="20220505", check_grammar=False):
  #replace print with, or add the call to the trrrBird block
  print(content)
  BASE = 'http://127.0.0.1:5000/'
  response = requests.post(BASE + "tweet", json={"content": content})


def processHUBcatalog(currentHUBCatalog, previousHUBCatalog):
  unique_blocks = []
  if len(previousHUBCatalog) == 0:
    print("Recording new HUB catalog")
    
  else: #we search for differences
    #unique_blocks = [car for car in currentHUBCatalog if car not in previousHUBCatalog]
    for car in currentHUBCatalog:
      if car not in previousHUBCatalog:
        unique_blocks.append(car)
        print("UNIQUE FOUND: " + car['slug'])
    content = "We have new BLOCKs in hub.balena.io! "
    for newBlock in unique_blocks:
      content = content + newBlock['slug'] + " | "
    if len(unique_blocks) > 0:
      notification(content + " (" + str(random.randint(0,10000000)) + ")")



try:
  api_key = os.environ['API_KEY']
except:
  print("ENVIRONMENT VARIABLES NOT AVAILABLE")
  quit()



previousHUBCatalog = catalog = []



# Configuring HUB call ONLY BLOCKS
baseURL = "https://api.balena-cloud.com/v6/application"
params= "$filter=is_of__class eq 'block'"
HUBurl = baseURL
HUBheaders = CaseInsensitiveDict()
HUBheaders["Authorization"] = "Bearer " + api_key
#HUBheaders["Content-Type"] = "application/json"


#looping queries HUB to detect CATALOG differences
while(1):
    
    #HUB
    try:
        resp = requests.get(HUBurl, headers=HUBheaders, params=params)
        catalog = resp.json()['d'].copy()
        
    except Exception as e:
        print("EXCEPTION accesing HUB.")
        print(e)
        quit()
    processHUBcatalog(catalog, previousHUBCatalog)
    previousHUBCatalog = catalog.copy()

    #SLEEP
    time.sleep(5)



    