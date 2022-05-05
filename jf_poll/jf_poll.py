import requests
import time
import os
import random
from requests.structures import CaseInsensitiveDict


def notification(content, date="20220505", check_grammar=False):
  #replace print with, or add the call to the trrrBird block
  print(content)
  BASE = 'http://127.0.0.1:5000/'
  response = requests.post(BASE + "tweet", json={"content": content})


def processJFimprovement(improvement, status):
    try:
        #newprogress = content['data'][0]['data']['milestonesPercentComplete']
        newstatus = improvement['data'][0]['data']['status']
        name = improvement['data'][0]['name']
        description = improvement['data'][0]['data']['description']

        if status == "":
            print("Registering initial JF status value: %s" %newstatus)
            status = newstatus
        else:
            if status != newstatus:
                print("Recording new JF status: %s" %newstatus)
                status = newstatus
                if status == "completed":
                    print("IMPROVEMENT COMPLETE")
                    content = "We have completed the %s improvement!! %s" %(name, description)
                    notification(content + " (" + str(random.randint(0,10000000)) + ")")
        return status
    except Exception as e:
        print("EXCEPTION accesing JF data. ")
        print(e)
        quit()




try:
  # improvement_id = "690875a6-2ac9-46bc-99f1-de195a326eae"
  # improvement_slug ="improvement-improvement-test-4166174"
  improvement_id = os.environ['IMPROVEMENT_ID']
  improvement_slug = os.environ['IMPROVEMENT_SLUG']
  bearer = os.environ['JF_TOKEN']
except:
  print("ENVIRONMENT VARIABLES NOT AVAILABLE")
  quit()



progress = -1
previousJFstatus = ""

# Configuring JF call
JFurl = "https://api.ly.fish/api/v2/query"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + bearer
headers["Content-Type"] = "application/json"

data = """
{
        "query":{"description":"Fetch all contracts linked to """ + improvement_slug + """","type":"object","required":["id","type"],"properties":{"id":{"const":\"""" + improvement_id + """"}},"$$links":{"is implemented by":{"type":"object","required":["type"],"additionalProperties":false,"properties":{"type":{"const":"project@1.0.0"}}}}},"options":{"limit":1,"mask":{"type":"object","required":["loop"],"properties":{"loop":{"enum":["loop-balena-io@1.0.0",null],"type":"string"}}}}
}
"""



#looping queries to JF and HUB to detect status changes and project differences
while(1):
    # JF
    try:
        resp = requests.post(JFurl, headers=headers, data=data)
        content = resp.json()
        
    except Exception as e:
        print("EXCEPTION accesing JF.")
        print(e)
        quit()

    previousJFstatus = processJFimprovement(content, previousJFstatus)


    #SLEEP
    time.sleep(5)



    