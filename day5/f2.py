#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ
import json
class Login(object):
	def __init__(self,username,passwd):
		self.username=username
		self.passwd=passwd
	def getUsername(self):
				return self.Username
	def setUsername(self,Username):
				self.Username=Username
	def getPasswd(self):
				return self.passwd
	def setPasswd(self,passwd):
				self.passwd=passwd

	def register(self):
		temp = self.username + '|' + self.passwd
		json.dump(temp,open('login','w'))
		print('注册成功')

	def login(self):
		f=str(json.load(open('login','r')))
		list1=f.split('|')
		if list1[0]==self.username and list1[1]==self.passwd:
			return True
		else:
			return False

	def userInfo(self):
		f=str(json.load(open('login','r')))
		list1=f.split('|')
		r=self.login()
		if r:
			print('欢迎{0}进入到系统'.format(list1[0]))
		else:
			print('对不起登录失败')
	def exit(self):
		import sys
		syy.exit(1)

def main():
	per = Login('hxj','hxj')
	while True:
		t=int(input('1.注册 2.登录 3.退出系统\n'))
		if t==1:
			per.register()
		elif t==2:
			per.userInfo()
		elif t==3:
			per.exit()
		else:
			print('输出错误 大傻逼')
			continue

# if __name__ == '__main__':
# 	main()

class Person(object):
	'''对人'''

	def info(self,username,paswd):
		'''
		获取用户信息
		:param username: 用户名
		:param paswd: 密码
		:return: 
		'''
		pass
print(Person.__doc__)

'''call方法对象创建时直接返回__call__内容 该方法可以模拟静态方法'''
class P1(object):
	def __new__(cls, *args, **kwargs):
		print('call方法')
per=P1()
#per()
'''__str__对象代表的含义 返回一个字符串 通过它可以把对象和字符串关联起来 方便某些程序的实现 该字符串表示某个类 实现了__str__后 可以直接使用print语句输出对象 也可以通过函数str来触发'''
class Son(object):
	'''我是一个雷'''
	def __str__(self):
		return self.__doc__

s=Son()
print(str(s))