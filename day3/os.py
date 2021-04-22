
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

import os

# print(os.system('netstat'))

#当前文件的目录
# print(dir(os))

# os.mkdir('c:/log')
# os.rmkdir('c:/log')
# 对文件目录的操作
# os.rename('c:/log','c:/newlog')

# 获取文件目录
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
#实现对day3下login文件内容的读取
base_dir=os.path.dirname(os.path.dirname(__file__))

print(os.path.join(base_dir,'Day3/login'))
f=open(os.path.join(base_dir,'Day3/login.txt'),'r')
print(f.read())


def f(*args,**kwargs):
	return kwargs

print(f(name='wuya',age='18'))

print(f(name='wuya',age='18',add='asfasfa'))