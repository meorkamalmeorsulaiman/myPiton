import requests
import pandas as pd

def getSiteId(orgId):

  url = "https://api.mist.com/api/v1/orgs/"+orgId+"/sites"

  payload={}
  headers = {
    'Authorization': 'Token [TOKEN]',
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data=payload).json()

  listSites = list()
  sitesName = list()

  for index in range(len(response)):
    listSites.append(response[index]["id"])

  return listSites



def connectedAp(siteId):

  url = "https://api.mist.com/api/v1/sites/"+siteId+"/stats/devices"

  payload={}
  headers = {
    'Authorization': 'Token [TOKEN]',
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data=payload).json() 

  df = pd.DataFrame(response)

  if df.empty == True:
    print("No APs Connected for: "+siteId)
    print("------------------------------------------------------------------------------------------")
  else:
    print("---------------------------"+siteId+"---------------------------")
    print(df.loc[df["status"] == "connected", ["name", "ip", "status", "uptime", "serial"]])
    print("------------------------------------------------------------------------------------------")



def main():
  orgId = "[ORG_ID]"
  allSites = getSiteId(orgId)
  for index in allSites:
    connectedAp(index)

if __name__ == "__main__":
  main()