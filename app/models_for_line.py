#!/usr/bin/env python3
#專門處理Line聊天機器人與使用者之間的互動
from app import line_bot_api, handler
from app.custom_models import PhoebeTalks
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):
	
	if event.source.user_id != "UdeadbeefUdeadbeefUdeadbeefUdeadbeef":
		
		reply = False
		
		if not reply:
			reply = PhoebeTalks.insert_record(event)
   
		if not reply:
			reply = PhoebeTalks.read_record(event)

		if not reply:
			reply = PhoebeTalks.user_list(event)
   
		if not reply:
			reply = PhoebeTalks.leaderboard(event)
   
		if not reply:
			reply = PhoebeTalks.record(event)
		
		if not reply:
			reply = PhoebeTalks.blood(event)
	
			
		if not reply:
			reply = PhoebeTalks.istock_reply(event)
			
		if not reply:
			reply = PhoebeTalks.pretty_echo(event)