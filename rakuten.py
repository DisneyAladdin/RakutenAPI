#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re
args = sZZys.argv
shopName = args[1]
counter = 0

payload = {
    'applicationId': ここにID入れてね,
    'hits': 30,
    'shopCode':shopName,
    'page':30,
    'postageFlag':1,
    }
r = requests.get(url, params=payload)
resp = r.json()
total = int(resp['count'])
Max = total/30 + 1
print "【num of item】",total
print "【num of page】",Max
print "==================================="

for i in resp['Items']:
	counter = counter + 1
	print '【No.】'+ PURPLE + str(counter) + ENDC
	item = i['Item']
	name = item['itemName']
	if len(name) >= 30:
		# 文字列の長さが３５文字以上であれば３５文字以降は省略
		print '【Name】' + OKGREEN + str(name[:30].encode('utf-8')) + '...' + ENDC
	else:
		print '【Name】' + OKGREEN + str(item['itemName'].encode('utf-8')) + ENDC
	print '【Price】' + CYAN + '¥' +str(item['itemPrice']) + ENDC
	
	# ポイント分（４倍）を差し引く
	#price = int(item['itemPrice'] * 0.96)
	print '【URL】',item['itemUrl']
	URL = item['itemUrl']
	print '【shop】',item['shopName']
	text = item['itemCaption']
	print text
	
	#JAN = ''
	#postCode_0 = re.findall('[0-9]{13}',URL)
	#if len(postCode_0) == 1:
	#	JAN = postCode_0[0]
	#    	print '【JAN】' + OKGREEN + str(JAN) + ENDC
	#	a.write(str(JAN)+','+str(name.encode('utf-8'))+','+str(price)+    ','+str(URL)+'\n')
	#else:
	#   	postCode = re.findall('[0-9]{13}',text)#extract JANcode
	#    	len_postCode = len(postCode)
	#    	if len_postCode == 1:
	#		JAN = postCode[0] 
	#		print '【JAN】' + WARNING + str(postCode[0]) + ENDC
	#		# Save if JAN code can be obtained.
	#		a.write(str(JAN)+','+str(name.encode('utf-8'))+','+str(price)+','+str(URL)+'\n')
	#   	else:
	#		JAN = 'NONE'
	#		print '【JAN】' + WARNING + 'JAN: NONE' + ENDC
	#    print ''
	#   sleep(0.1)
