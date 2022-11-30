import json

import pandas as pd
import requests

url = "https://api.mist.com/api/v1/sites/[TOKEN]/devices?type=all"

payload={}
headers = {
  'Authorization': 'Token [TOKEN]',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

df = pd.DataFrame(response)
header = ["id", "serial"]
df.to_csv('data/switchesId.csv', columns = header)

listHostname = pd.read_csv("data/switchesHostname.csv")
listSwitchesId = pd.read_csv("data/switchesId.csv")
for i in range(len(listHostname)):
    listSerialNum = listHostname.loc[i, 'swSerialNumbers']
    listSwitchesHostname = listHostname.loc[i, 'switchHostname']
    for j in range(len(listSwitchesId)):
        listMistSerialNum = listSwitchesId.loc[j , 'serial']
        if listSerialNum == listMistSerialNum:
            
            switchId = listSwitchesId.loc[j, 'id']
            
            url = "https://api.mist.com/api/v1/sites/[SITE_ID]/devices/"+switchId
            
            payload = json.dumps({
                  "name": ""+listSwitchesHostname+""
                  })
            headers = {
            
                  'Authorization': 'Token [TOKEN]',
                  'Content-Type': 'application/json'
            }
            
            response = requests.request("PUT", url, headers=headers, data=payload)
            
            print(response.text)
