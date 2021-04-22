#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

#动态参数
'''
需求:
1.对请求参数进行ascill排序
2.排序后，对请求参数进行md5的加密

1.写一个函数，获取请求参数，对请求参数进行加密
'''
# dict1={'name':'hxj','age':18,'data':{
#        'name':'wuya','age':18}}
# def data(**kwargs):
#        return dict(sorted(kwargs.items(),key=lambda item:item[0]))

# dict1={'name':'hxj','age':18,'data':{
#        'name':'wuya','age':18}}
# dict2={'name':'hxj','age':18,'address':'chengdu','work':'tester'}
# print(data(**dict2))
#
# def f():
#        print('Hello world')
#函数可以是变量
# per=f()
# per
#函数可以是参数
# def f1(a):
#        return a
# f1(f())

# def f1(*arg,**kwargs):
# 	print(arg,kwargs)
#
# f1([1,2,3])
# f1('a')
# f1(name='wuya')
# f1(dict1={'name':'wuya'})
#
# def f(a,b=None):
#        print()
#
# def getFile(director='d:/',fileName=None):
#        pass
# getFile(fileName='.xml')

'''
返回值
1.None
2.return后面的内容就是函数的返回值
'''

def f():
       print('hello world')
#print(f())

def add(a,b):
       return a+b
#print(add(2,3))

# def login():
#        username=input('请输入登录账号\n')
#        password=input('请输入账号的密码\n')
#        if username=='hxj' and password=='123456':
#               return 'sdtytugi43567szxgd'
#
# def profile(session):
#        if session==login():#返回值为session
#               print('欢迎访问')
#        else:
#               print('未登录系统，跳转到登录的界面 302')
#
# profile('sdtytugi43567szxg')

'''
全局作用域：全局变量
局部作用域：针对局部
先看自己内部，再回父部
'''

# name='wuya'
#
# def f():
#        global name
#        name='wuyya'
#        print(name)
#
# f()

# def f():
#        name='我是父函数'
#        def f1():
#               name='我是子函数的值'
#               print(name)
#        return f1()
#
# f()

# per=lambda a,b:a+b
#
# print(per(2,3))

age=10
#print('true') if age>5 else print('false')

# login=lambda username,password:print('登录成功') if username=='hxj' and password=='123456' else print('error')
#
# login('hxj','123456')

# data=lambda **kwargs:dict(sorted(kwargs.items(),key=lambda item:item[0]))
#
# print(data(name='admin',age=18))

list1=[1,2,3,4,5]

def f():
       list2=[]
       for i in list1:
              i+=100
              list2.append(i)

       print(list2)

#f()

# def f(a):
#        return a+100
#
# print(list(map(f,list1)))
# print(list(map(lambda a:a+100,list1)))
def f():
       list2=[]
       for i in list1:
           if i>3:
              list2.append(i)

       print(list2)

print(list(filter(lambda a:a>1,list1)))