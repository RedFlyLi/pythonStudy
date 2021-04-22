#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ


'''
1、函数可以当做一个变量
2、函数的参数也可以是函数
3、函数是可以嵌套的
'''
#1、函数可以当做一个变量
# def f():
# 	print('hello')
#
# per=f()
# per
# #2、函数的参数也可以是函数
# def f2(a):
# 	return a
# #f2(f())
#
# def login(username='hxj',password='123456'):
# 	if username=='hxj' and password=='123456':
# 		return 'sdtytugi43567szxgd'
#
# def profile(token):
#        if token=='sdtytugi43567szxgd':
#               return '欢迎访问'
#        else:
#               return '未登录系统，跳转到登录的界面 302'
#
# print(profile(login()))

# def f3():
# 	def f4():
# 		print('hello')
# 		return '111'
# 	return f4()
#
# print(f3())

# def getInfo(func):
# 	def inner():
# 		print('1111')
# 		func()
# 	return inner
#
# @getInfo
# def f1():
# 	print('22222')

#f1()
#先执行装饰器 并且此时被装饰的函数是装饰器函数的参数
'''
步骤：
执行getinfo函数的时候，把被装饰的函数f1当做参数来传递
getinfo函数的返回值会重新赋值
一旦结合了装饰器后，调用f1的函数其实执行的是inner函数的内部，原来函数f1被覆盖
被装饰的函数f1重新赋值给装饰器的内层函数inner
'''

def login(func):
	def inner(token='asdf'):
		if token=='asdf':
			return func(token)
		else:
			return '请登录'
	return inner

@login
def profile(token):
	return '个人主页'

print(profile('asdf'))

def outer(func):
	def inner(*args,**kwargs):
		print(args,kwargs)
		func()
	return inner()