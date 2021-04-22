#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import json
import requests
'''
序列化：把python的数据类型转为str的类型过程
反序列化：把str的数据类型转为python的数据结构（字典）
'''

dict1= {"name":'sundy','age':18,'gender':'男','hobby':'同桌'}

#  print(type(dict1))
#
# r=requests.post(url='https://www.fxiaoke.com/FHH/EM0HUL/Authorize/PersonalCloudLogin?_fs_token=',
# 				data={"phoneNumber":"17723984804","internationalAreaCode":"+86","rsaPassword":"dAlC55LiQRw3wQkmy2xnVIzFKNQUOfu7Z/1vWjTYJWuapOEvRPH4Pw3SvUT8Xb19v7elhAsrboGERncR4T/xB8flbSeU4MUkAOretpgeqya7nnuepVXdpTi4bJ1etuYz8QDmqomhVV1MoyGRQu0z3GP9SplW4pvXZx1x1t4h9Yw=","persistenceHint":True,"deviceId":"411603b71d577ed2af3e333ef6260016","publicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB"},
#                 headers={'content-type':'application/login'})
#
# print(r.status_code)

#序列化：dict--->str
# dict_str=login.dumps(dict1)
# print(dict_str,type(dict_str))
#
# #反序列化：str--->dict
# str_dict=login.loads(dict_str)
# print(str_dict,type(str_dict))
#
# #列表的序列化和反序列化
# list1=['admin','hh','xx']
#
# #序列化：list--->str
# list_str=login.dumps(list1)
# print(list_str,type(list_str))
#
# #反序列化：str--->list
# str_list=login.loads(list_str)
# print(str_list,type(str_list))

#元组的序列化和反序列化
# tuple1=(1,2,3)
# print(tuple1,type(tuple1))
#
# tuple_str=login.dumps(tuple1)
# print(tuple_str,type(tuple_str))
#
# str_tuple=login.loads(tuple_str)
# print(str_tuple,type(str_tuple))

'''文件的序列化和反序列化'''
r=requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
#print(r.content.decode('utf-8'))
#把服务端的响应数据写到文件中
from MyEncoder import MyEncoder
json.dump(r.content,open('weather.login','w',),cls=MyEncoder,indent=4)
#把文件中的数据取出来反序列化读取文件的内容
# dict1=login.load(open('weather.login','r'))
# print(dict1,type(dict1))

#将文件反序列化出来的数据转为成数据结构
dict1=json.loads((json.load(open('weather.login','r'))).encode('UTF-8'))
print(dict1['weatherinfo']['city'])