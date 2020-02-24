import pyrebase
import json
import pandas as pandas
import os
import cv2
from collections import OrderedDict,Counter
import matplotlib.pyplot as plt
import itertools
import numpy as np
from operator import itemgetter
from flask import Flask, render_template
app = Flask(__name__)

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

with open('swiss_ranks_data.json', 'r') as f:
	data = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#db.child("parts").push(data)
allCats = db.child("parts").get()
#data = pd.DataFrame(allCats.val())

data=allCats.val()
data = json.loads(json.dumps(data))
data = sorted(data["-M0RfTUEabjwpA8SdTH1"], key=itemgetter('Status'))

@app.route('/')
def home():
	return render_template('index.html',color="#3a6f99",url="static/images/logo.png")

@app.route('/engineer')
def engineer():
  status=[]
  parts=[]
 # print(data)
  plt.cla()
  plt.clf()
  for key in data:
    val=key['Created By']
    status.append(val)

  parts=Counter(status) 
  status=list(parts.keys() )
  parts=list(parts.values())
  #print(status,parts)
  y_pos = np.arange(len(status))
  plt.barh(y_pos, parts, align='center', alpha=0.5)
  plt.yticks(y_pos, status)
  plt.xlabel('Usage')
  plt.savefig(os.path.join('static', 'images', 'new_plot.png'))
  return render_template('index.html', url ='/static/images/new_plot.png',color='#4e995f')
  #plt.show()
 # plt.savefig("barEngineer.jpg")
   
  #im=cv2.imread("barEngineer.jpg")
  #cv2.imshow("adsfs",im)
  #cv2.waitKey(0)

@app.route('/bar')
def statusbar():
    status=[]
    parts=[]
    plt.cla()
    plt.clf()
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
    plt.savefig(os.path.join('static', 'images', 'bar.png'))
    return render_template('index.html', url ='/static/images/bar.png',color='#ce6464')

@app.route('/pie')
def statuspie():
    status=[]
    parts=[]
    plt.cla()
    plt.clf()
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
    labels=[] 
    print(status,parts)
#status=set(status)
    for i in range(len(status)):
     la=status[i]+","+str(parts[i])
     labels.append(la)
    plt.pie(parts, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

#plt.show()
    plt.savefig(os.path.join('static', 'images', 'pie.png'))
    return render_template('index.html', url ='/static/images/pie.png',color='#e9ca6f')

@app.route('/approve')
def approve():
  status=[]
  parts=[]
 # print(data)
  plt.cla()
  plt.clf()
  for key in data:
    val=key['Approve or Reject By']
    status.append(val)

  parts=Counter(status) 
  status=list(parts.keys() )
  parts=list(parts.values())
  #print(status,parts)
  y_pos = np.arange(len(status))
  plt.barh(y_pos, parts, align='center', alpha=0.5)
  plt.yticks(y_pos, status)
  plt.xlabel('Usage')
  plt.savefig(os.path.join('static', 'images', 'aprove.png'))
  return render_template('index.html', url ='/static/images/aprove.png',color='#4ca9bc')



if __name__ == '__main__':
   app.run(debug = True)  
