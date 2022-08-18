#!/usr/bin/env python3

alpaca_blue = '#066BAF'

def image_in_FlexMessage(url):
	return {"type": "image",
			"url": url,
			"size": "full",
			"aspect_ratio": "20:13",
			"aspect_mode": "cover"}
			
def text_in_FlexMessage(text, size, color, weight='regular', wrap=False):
	return {"type": "text",
			"text": text,
			"size": size,
			"color": color,
			"weight": weight,
			"wrap": wrap }
			
def logo_in_FlexMessage(text='紅色救援'):
	return text_in_FlexMessage(text, size='md', color=alpaca_blue, weight='bold')

def title_in_FlexMessage(text):
	return text_in_FlexMessage(text, size='xl', color='#555555', weight='bold')

def heading_in_FlexMessage(text):
	return text_in_FlexMessage(text, size='xl', color='#555555')

def note_in_FlexMessage(text):
	return text_in_FlexMessage(text, size='md', color='#AAAAAA', wrap=True)

def separator_in_FlexMessage(margin='xl'):
	return {"type": "separator", "margin": margin}

def button_in_FlexMessage():
	return {"type": "button",
        	"style": "link",
        	"height": "sm",
        	"action": {
          	"type": "uri",
          	"label": "新增個人資料",
          	"uri": "https://liff.line.me/1657366253-D9Zk1m7l"}}
 
def button_in_FlexMessage_list(user_id):
    ID = str(user_id)
    return {"type": "button",
        	"style": "link",
        	"height": "sm",
        	"action": {
          	"type": "uri",
          	"label": "個人資料列表",
          	"uri": "https://dry-lake-70751.herokuapp.com/list/"+ID}}
			
def index_FlexMessage(user_id):
	hero_image_url = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png'
	body_contents = [logo_in_FlexMessage(), 
					title_in_FlexMessage('個人資料'), 
					separator_in_FlexMessage()]
					#heading_in_FlexMessage('Overall'), 
					#note_in_FlexMessage('# 查詢所有資料'),
					#heading_in_FlexMessage('單筆資料'), 
					#note_in_FlexMessage('查詢單筆資料'),
#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# 按照 training 查詢'), 
					#separator_in_FlexMessage()]
	footer_contents = [button_in_FlexMessage(),
						button_in_FlexMessage_list(user_id)]
#                       button_in_FlexMessage('training', 'training')]
	FlexMessage = {'type': 'bubble',
					'hero': image_in_FlexMessage(hero_image_url),
					'body': {
						'type': 'box', 
						'layout': 'vertical', 
						'spacing': 'md', 
						'contents':body_contents},
					'footer': {
						'type': 'box',
						'layout': 'vertical',
						'contents': footer_contents}}
	return FlexMessage

