#!/usr/bin/env python3

import random
import urllib
import re
import datetime

def prepare_record(text):
	text_list = text.split('\n')
	
	year = text_list[0].split(' ')[0].split('/')[0]
	month = text_list[0].split(' ')[0].split('/')[1]
	day = text_list[0].split(' ')[0].split('/')[2]
	d = datetime.date(int(year), int(month), int(day))
	
	record_list = []
	
	for i in text_list[1:]:
		items = i.split(' ')
		
		name = items[0]
		type = items[1]
		
		record = (name, type,str(d))
		record_list.extend(record)

		
	return record_list

def istock_isch(target):
	target = urllib.parse.quote(target)
	
	url = f'https://www.istockphoto.com/photos/{target}?pharse={target}&sort=mostpopular'
	print(url)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	
	req = urllib.request.Request(url,headers=headers)
	page = urllib.request.urlopen(req).read()
	
	pattern = 'src="(https://media.*?)"'
	img_list = []
	for match in re.finditer(pattern, str(page)):
		print(match.group(1))
		img_list.append(re.sub('amp;','',match.group(1)))
		
	print(len(img_list))
	random_img_list = set(random.choices(img_list, k=5))
	
	return img_list[random.randint(0, len(img_list) -1)], random_img_list