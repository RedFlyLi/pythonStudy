#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

'''
根据字符串的形式去某个模块中寻找东西--->getottr()
根据字符串的形式去某个模块中判断是否存在--->hasattr()
根据字符串的形式去某个模块中设置东西--->setottr()
根据字符串的形式去某个模块中删除东西--->delottr()
'''

#通过__import__导入目标模块,并且放在对象f中
# f=__import__('login')
#通过对象找login模块中index的字符串并且调用
# f.index()

import login

#第一个参数时模块 第二参数时函数名
# f=getattr(login,'logout')
# f()

#如何找到Person中的info方法并且调用它
# obj=login.Person()
# if hasattr(obj,'info'):
# 	f=getattr(obj,'info')
# 	f()
# else:
# 	print('找不到')

obj=login.Person()
f1=setattr(obj,'exit','this is a exit function')
print(f1)
f2=hasattr(obj,'exit')
print(f2)



# f=setattr(login,'str2','hello')
# if hasattr(login,'str2'):
# 	f2=getattr(login,'str2')
# 	print(f2)
# else:
# 	print('wu')
