#Reverse lookup script

import pandas as pd
import socket
data = pd.read_csv("data/switches.csv")
# hostname = data['Hostname'].astype(str) + ".example.domain]"

for i in range(len(data)):
    ipAddr = data.loc[i, 'IP Address']
    print(socket.gethostbyaddr(ipAddr)[0], socket.gethostbyaddr(ipAddr)[2])