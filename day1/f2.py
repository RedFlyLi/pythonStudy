#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

'''
注册账户，然后注册的账户登录到登录系统后，显示出登录的昵称
1.注册的函数
2.登录的函数
3.获取昵称的函数
'''
def inOut():
	username=input('请输入账号:\n')
	password=input('请输入密码:\n')
	return username,password

def register():
	username,password=inOut()
	temp=username+ '|'+ password
	with open('login.md','w')as f:
		f.write(temp)
		f.close()

def login():
	username,password=inOut()
	with open('login.md','r') as f:
		info=f.read()
	info=info.split('|')
	if username==info[0] and password==info[1]:
		return True
	else:
		return False

def getNick(func):
	with open('login.md','r') as f:
		info=f.read()
	info=info.split('|')
	if func:
		print('{0}你好 欢迎光临'.format(info[0]))
	else:
		print('请登录系统')

#register()
#print(login())

# print(getNick(login()))

def main():
	while True:
		t=int(input('1.注册 2.登录 3.退出系统\n'))
		if t==1:
			register()
		elif t==2:
			getNick(login())
		elif t==3:
			import sys
			sys.exit(1)
		else:
			print('输出错误 大傻逼')
			continue

if __name__ == '__main__':
	main()