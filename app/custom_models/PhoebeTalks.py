#!/usr/bin/env python3
from app import line_bot_api
from app.custom_models import utils, CallDatabase, PhoebeFlex, Leaderboard, Record

from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, FlexSendMessage
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn, URIAction
import json
import random


def insert_record(event):
	
	if '紀錄捐血' in event.message.text:
		try:
			record_list = utils.prepare_record(event.message.text)
			if record_list[0] !="" and record_list[1] != "" and record_list[2]!="":
				try:
					user_id = event.source.user_id
					result = CallDatabase.insert_record(user_id,record_list)
					CallDatabase.leaderboard(user_id,record_list)
					line_bot_api.reply_message(
						event.reply_token,
						TextSendMessage(text=result)
					)
					return True
				except:
					return True
			else:
				line_bot_api.reply_message(
					event.reply_token,
					TextSendMessage(text='格式錯誤!請重新輸入')
				)
				return True
			
			return True
		except:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='失敗了!')
			)
			return True
		
	else:
		return False

def read_record(event):
	if '查詢紀錄' in event.message.text:
		try:
			print('a')
			result=[]
			user_id = event.source.user_id
			result = CallDatabase.read_record(user_id)
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text=str(result))
			)
			return True
		except:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='失敗了!')
			)
			return True
	else:
		return False

def user_list(event):
    if '個人資料' in event.message.text:
        try:
            #json_file = open('app/card.jsons', 'r')
            #FlexMessage = json.load(json_file)
            user_id = event.source.user_id
            line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage('profile', contents=PhoebeFlex.index_FlexMessage(user_id))
        	)
            return  True
        except:
            line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='失敗了!')
			)
            return True
    else:
        return False
    
def leaderboard(event):
    if '排行榜' in event.message.text:
        try:
            #json_file = open('app/card.jsons', 'r')
            #FlexMessage = json.load(json_file)
            line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage('profile', contents=Leaderboard.index_FlexMessage())
        	)
            return True
        except:
            line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='失敗了!')
			)
            return True
    else:
        return False
    
def record(event):
    if '紀錄' in event.message.text:
        try:
            #json_file = open('app/card.jsons', 'r')
            #FlexMessage = json.load(json_file)
            user_id = event.source.user_id
            line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage('profile', contents=Record.index_FlexMessage(user_id))
        	)
            return  True
        except:
            line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='失敗了!')
			)
            return True
    else:
        return False
    
def blood(event):
    if '缺血熱區' in event.message.text:
        try:
            user_id = event.source.user_id
            picture = CallDatabase.read_db(user_id)
            message = ImageSendMessage(original_content_url=picture,
                                       preview_image_url=picture)
            line_bot_api.reply_message(event.reply_token, message)
            
            return True
        except:
            user_id = event.source.user_id
            print(user_id)
            result = CallDatabase.area_blood(user_id)
            #print(result)
            if result is None:
            #if not result.get('地區') or result.get('血型'):
                line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text='請先新增個人資料！'))
                
            else:
                line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text='發生錯誤！'))
            #line_bot_api.reply_message(event.reply_token,
                                       #TextSendMessage(text='發生錯誤！'))
            return True
        
    else:
        return False

	
def istock_reply(event):
	
	try:
		target = event.message.text
		img_url, random_img_list = utils.istock_isch(target)
		img_template = ImageCarouselTemplate(
			columns=[ImageCarouselColumn(image_url=url, action=URIAction(label=f'image{i}', uri=url)) for i, url in enumerate(random_img_list)])
		print(img_url)
		line_bot_api.reply_message(
			event.reply_token,
			TemplateSendMessage(
				alt_text=f'ImageCarousel template {target}',
				template=img_template
			)
		)
			
		return True
	
	except:
		return False
	
def pretty_echo(event):
	if '捐血紀錄' in event.message.text:
		try:
			result ="1.若要輸入捐血紀錄，請照下列格式輸入: \n\'捐血日期\' 紀錄捐血：\n\'姓名\' \'本次捐血方式\'\n範例：2022/1/1 紀錄捐血：\n王小明 250cc全血\n2.若要查詢捐血紀錄，請輸入\'查詢紀錄\'"
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text=result)
			)
			return True
		except:
			return True
	else:
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=event.message.text)
		)
		
		return False
	
	