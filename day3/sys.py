#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import sys
# print(sys.argv)
# if sys.argv[1]=='sleep':
# 	print('sleep')
# else:
# 	print('end')
# print(dir(sys))
print(sys.version)
print(sys.platform)

for item in sys.path:
	print(item)

'''
	标准库：F:\python37\lib
	第三方的库：F:\python\lib\site-packages
	自定义的库：
'''

sys.path.append('C:\\Users\\ASUS\\PycharmProjects\\untitled4\\day2')

for item in sys.path:
	print(item)

# from day2.second import *
#
# logingin()