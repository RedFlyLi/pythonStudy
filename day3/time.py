#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import time as t

#获取时间戳
print(int(t.time()))

#获取当前实际
print(t.localtime(t.time()))
print(t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))

nowTime=t.strftime('%y-%m-%d %H:%M:%S',t.localtime())

t.sleep(2)
print(nowTime)
