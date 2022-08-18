#!/usr/bin/env python3
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

#Line聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot','channel_access_token'))
handler = WebhookHandler(config.get('line-bot','channel_secret'))

app.jinja_env.add_extension('jinja2.ext.do')
#最後再把分散的程式碼呼叫進來
from app import routes,models_for_line