import pyrebase
import json
import pandas as pd
import os
import cv2
from collections import OrderedDict,Counter
import matplotlib.pyplot as plt
import itertools
import numpy as np
from operator import itemgetter
from flask import Flask, render_template

def engineer(data):
  status=[]
  parts=[]
  #print(data)
  for key in data:
    val=key['Created By']
    status.append(val)

  parts=Counter(status) 
  status=list(parts.keys() )
  parts=list(parts.values())
  print(status,parts)
  y_pos = np.arange(len(status))
  plt.barh(y_pos, parts, align='center', alpha=0.5)
  plt.yticks(y_pos, status)
  plt.xlabel('Usage')
  plt.show()
  plt.savefig("barEngineer.jpg")
  im=cv2.imread("barEngineer.jpg")
  cv2.imshow("adsfs",im)
  cv2.waitKey(0)

config = {
    "apiKey": "AIzaSyBO7y8zvprbbLv-fxCIWg-c4fuk7QoWIV8",
    "authDomain": "swiss-ranks.firebaseapp.com",
    "databaseURL": "https://swiss-ranks.firebaseio.com",
    "projectId": "swiss-ranks",
    "storageBucket": "swiss-ranks.appspot.com",
    "messagingSenderId": "466052251944",
    "appId": "1:466052251944:web:9f3cd63b927d883fff901d",
    "measurementId": "G-E2V4NGM0FJ",
    "serviceAccount": "credentials/serviceAccountCredentials.json"
}    




plt.cla()
plt.clf()
with open('swiss_ranks_data.json', 'r') as f:
	data = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#db.child("parts").push(data)
allCats = db.child("parts").get()
data = pd.DataFrame(allCats.val())

data=allCats.val()
data = json.loads(json.dumps(data))
#print(data["-M0RfTUEabjwpA8SdTH1"])
#data = json.loads(data[0][0])

parts=[]
status=[]
for i in data["-M0RfTUEabjwpA8SdTH1"]:
	parts.append(i["Part Number"])
	status.append(i["Status"])
data = sorted(data["-M0RfTUEabjwpA8SdTH1"], key=itemgetter('Status'))
#print(data)
print("gotit") 
# Display data grouped by `class`

status=[]
parts=[]
for key, value in itertools.groupby(data, key=itemgetter('Status')):
    status.append(key)
    count = 0
    print(key)
    #parts.append(len(value))
    for i in value:
        #print(i.get('Part Number'))
        count+=1
    parts.append(count)
    print(count)
    count=0
print(status,parts)
#status=set(status)
y_pos = np.arange(len(status))
plt.barh(y_pos, parts, align='center', alpha=0.5)
plt.yticks(y_pos, status)
plt.xlabel('Usage')
#p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#df = pd.DataFrame({parts,status})
#plt.xticks(parts, status)
#plt.show()
plt.savefig('foo.jpg')
values=[]
sum1=sum(parts)
for i in parts:
	per=(i*100)//sum1
	values.append(per)

explode = (0, 0, 0, 0,0)  
print(status,parts)
labels=[]
for i in range(len(status)):
	la=status[i]+","+str(parts[i])
	labels.append(la)
print(labels)
plt.cla()
plt.clf()
plt.pie(parts, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

#plt.show()
plt.savefig('pie.jpg')

plt.cla()
plt.clf()
engineer(data)