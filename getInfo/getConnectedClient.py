import requests
import json
import pandas as pd
import ast

url = "https://api.mist.com/api/v1/sites/[SITE_ID]/stats/clients"

payload={}
headers = {
  'Authorization': 'Token [TOKEN_ID]',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

df = pd.DataFrame(response)
print(df[["username", "hostname", "mac", "ssid", "ip", "rssi", "proto", "band", "os"]])




  