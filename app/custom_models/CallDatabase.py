#!/usr/bin/env python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate('blood-48be6-firebase-adminsdk-qu8br-a96b64eb95.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()


def insert_record(user_id,record_list):
	data = {
	'姓名': record_list[0],
	'捐血方式': record_list[1],
	'時間': record_list[2],
    }
	collection_ref = db.collection(str(user_id))
	collection_ref.add(data)

	message = f"資料成功匯入囉!"
	
	return message

def leaderboard(user_id,record_list):
    data ={
        '姓名': record_list[0],
        record_list[1]:firestore.Increment(1)
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    blood_ref.update(data)

def read_record(user_id):
    docs = db.collection(str(user_id)).stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        datalist.append(doc.to_dict())
        #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def insert_userlist(user_id,nm,blood,year,gender,place,other):
    data ={
	'暱稱':nm,
	'血型':blood,
	'出生年':year,
	'性別':gender,
    '地區':place,
	'備註':other
	}
    collection_ref = db.collection('個人資料').document(str(user_id))
    collection_ref.set(data)

def read_userlist(user_id):
    #user_id = event.source.user_id
    collection_ref = db.collection('個人資料').document(str(user_id))
    datalist=[]
    docs = collection_ref.get()
    datalist.append(docs.to_dict())
    #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def read_leaderboard():
    docs = db.collection('捐血次數').stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        #docc = doc.to_dict()
        datalist.append(doc.to_dict())
        #datalist.append([docc['姓名'], docc['250cc全血']])
        #print(docc['姓名'])
        #print(docc['250cc全血'])
        #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def record(user_id,year,way):
    data ={  
	'時間':year,
	'捐血方式':way
	}
    print(user_id)
    collection_ref = db.collection(str(user_id))
    collection_ref.add(data)
    
def r_leaderboard_n(user_id,nm):
    data ={
        '姓名': nm,
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    docs = blood_ref.get()
    datalist={}
    datalist = docs.to_dict()
    if not datalist:
         blood_ref.set(data)
    else:
        blood_ref.update(data)

def r_leaderboard(user_id,way):
    data ={
        way:firestore.Increment(1)
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    blood_ref.update(data)


def r_record(user_id):
    docs = db.collection(str(user_id)).stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        datalist.append(doc.to_dict())
        #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

# 到firebase讀到對應血型與地區後，將bloodStateNumber設為缺血數字，並將picture設為對應捐血寶寶圖片
def read_db(user_id):
    read_collection_name = "bloodTable"
    document_name = str(datetime.date.today())
    # yourBloodType 和 yourRegion 要到資料庫內爬抓使用者的血型與地區，目前先給個固定值
    print(user_id)
    collection_ref = db.collection('個人資料').document(str(user_id))
    datalist=[]
    docs = collection_ref.get()
    #datalist.append(docs.to_dict())
    docc = docs.to_dict()
    #print(datalist)
    #print(docc['血型'])
   # print(docc['地區'])
    yourBloodType = docc['血型']
    yourRegion = docc['地區']
    yourRegion_yourBloodType = yourRegion + "_" + yourBloodType
    read_collection = db.collection(read_collection_name).document(
        document_name)
    doc = read_collection.get()
    bloodStateNumber = format(doc.to_dict()[yourRegion_yourBloodType])

    if bloodStateNumber == "0":
        picture = "https://firebasestorage.googleapis.com/v0/b/bloodtable-19d4e.appspot.com/o/redblood.jpg?alt=media&token=92e3b419-4ae3-44c9-8a9f-478fb244c9e0"
    elif bloodStateNumber == "1":
        picture = "https://firebasestorage.googleapis.com/v0/b/bloodtable-19d4e.appspot.com/o/yellowblood.jpg?alt=media&token=8461a6d8-6088-4905-86ee-fd36fe1427c4"
    else:
        picture = "https://firebasestorage.googleapis.com/v0/b/bloodtable-19d4e.appspot.com/o/greenblood.jpg?alt=media&token=673c62a3-e601-425c-a6fc-05b83f058732"
    return picture

def area_blood(user_id):
    collection_ref = db.collection('個人資料').document(str(user_id))
    docs = collection_ref.get()
    datalist={}
    datalist = docs.to_dict()
    #if datalist[0]['地區'] or datalist[0]['血型'] is None:
    #print(datalist)
    return datalist