from time import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import requests
import bs4
import datetime
import logging
from flask import Flask, request, abort
from app.custom_models.CallDatabase import db


sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def scheduled_job():
    url = 'https://www.blood.org.tw/Internet/main/index.aspx'
    htmlFile = requests.get(url)

    if htmlFile.status_code == requests.codes.ok:
        print("success")
    else:
        print("fail")

    objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
    objTag = objSoup.find(id='blood-table')
    objShow = objTag.find_all("tr")
    # print(objShow)

    array = {}
    #CallDatabase.bloodtable
    collection_name = "bloodTable"
    document_name = str(datetime.date.today())
    collection_ref = db.collection(collection_name).document(document_name)
    collection_ref.set(None)

    for i in range(2, 6):
        objimg = objShow[i].find_all("img")  #objShow[2]:A型...objShow[5]:AB型

        if i == 2:
            bloodType = "A型"
        elif i == 3:
            bloodType = "B型"
        elif i == 4:
            bloodType = "O型"
        else:
            bloodType = "AB型"

        #app.logger.info(bloodType)
        # print(bloodType)

        for j in range(0, 5):
            # print(objimg[j]['src'])

            if j == 0:
                region = "台北"
            elif j == 1:
                region = "新竹"
            elif j == 2:
                region = "台中"
            elif j == 3:
                region = "台南"
            else:
                region = "高雄"

            region_bloodType = region + "_" + bloodType

            if objimg[j]['alt'] == "庫存量4日以下":
                number = "0"
            elif objimg[j]['alt'] == "庫存量4到7日":
                number = "1"
            else:
                number = "2"
            # array[region]=objimg[j]['src']
            array[region_bloodType] = number
            # collection_ref.set(array)
            #CallDatabase.f_bloodtable(array)
            collection_ref.update(array)
            #app.logger.info(region + ":" + number)
            # print(region+":"+number)
            # print(array)
            array = {}
    # print('This job is run every three minutes.')


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()