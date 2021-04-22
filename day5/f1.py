#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

'''类 是由一系列属性和方法组成的'''
class F1(object):
	pass

'''
#对象的创建---->就是类实例化的过程
1.对象的句柄，区分不同的对象
2.属性:
	公有属性public
			类属性:属于类也属于对象 建议使用类调用
			实例属性：只属于对象
			局部变量
	私有属性private
3.方法
'''
# f1=F1()
# f2=F1()

# print(id(f1))
# print(id(f2))
'''self=this'''
# class Person(object):
# 	contry='zhongguo'
# 	def __init__(self,name,age):
# 		#实例属性
# 		self.name=name
# 		self.age=age
# 		#局部变量
# 		# zone=u"空间"
# 	def getName(self):
# 		return self.name
# 	def setName(self,name):
# 		self.name=name
# 	def getAge(self):
# 		return self.age
# 	def setAge(self,age):
# 		self.age=age
# 	def info(self):
# 		return 'name:{0},age:{1},guojia:{2}'.format(self.getName(),self.getAge(),self.contry)
#
# per=Person('wuya',18)
#
# print(per.age,per.name)
# per.setName('lisa')
# per.setAge('23')
# print(per.age,per.name)
#
# print(per.info())

# class Person(object):
	# def __init__(self,*args,**kwargs):
		# self.kwargs=kwargs
		# self.args=args
	# def info(self):
		# print(self.kwargs)
		# print(u'信息',self.kwargs.values())
		# print(self.args)

# per1=Person(name='hxj1')
# per1.info()
#
# per2=Person(name='hxj',age=18)
# per2.info()
#
# per3=Person(name='hxj2',age=18,isMarry='yes')
# per3.info()

# per4=Person('naem',18,'cd')
# per4.info()


'''构造函数
不管一个类是否写了构造函数，他都是有构造函数的
一个类可以有多个构造函数 建议一个类只有一个构造函数
1.初始化属性
'''
# class Person(object):
	# pass
	# def __init__(self):
		# print('我是构造函数')
		# self.name=name
		# self.age=age

	# def info(self):
		# print('我是调用的方法')
	#
	# def __init__(self,address):
	# 	self.address=address

	# def __del__(self):
		# print('我是析构函数')

# per=Person('hxj',11)
# per=Person('cd')

#对象实例化 先执行构造函数 对象调用的方法 代码跳转到具体的方法 执行方法的代码块 最后执行析构函数
#per=Person()

#per.info()

'''普通方法 特性方法'''
# class Person(object):
# 	def conn(self,user,passwd,host,port):
# 		pass
# 	def info(self):
# 		print('我是普通方法')
# 	def f1(self,*args,**kwargs):
# 		pass
#
# per=Person()
# # per.conn()
# per.f1()
# per.f1('admin')

'''特性方法:这个方法不能有形式参数'''
class Person(object):

	@property
	def getUserID(self):
		pass

per=Person()
per.getUserID

# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.find_element_by_id('').text

'''静态方法:直接使用类名来进行调用 同时对象也可调用'''
class Person(object):
	@staticmethod
	def conn(user):
		pass

Person.conn('hxj')


'''
类方法：直接使用类来进行调用，属于类
'''
class Person(object):
	@classmethod
	def conn(cls):
		pass

'''
属于类：
类属性
静态方法
类方法

属于对象：
实例属性
普通方法
特性方法
'''

'''
继承：重用以及存在的数据和行为，减少代码的重复编写
子类继承父类的所有实例变量和方法
'''

'''
类属性的继承
'''

# class Person(object):
# 	country='中国'
#
# class UsaPerson(Person):
# 	pass
#
# per=UsaPerson
# per.country
#子类需要继承父类的实例属性可以继承也可不继承 但类属性没有选择
# class Fruit(object):
# 	def __init__(self,name):
# 		self.name=name
#
# class Apple(Fruit):
# 	def __init__(self,name,pingppai,color):
# 		# Fruit.__init__(self,name)
# 		super(Apple, self).__init__(name)
# 		#super的方式
# 		self.pingppai=pingppai
# 		self.color=color
#
# 	def info(self):
# 		print('{0},{1}'.format(self.name,self.pingppai))
#
# apple=Apple('苹果','品牌','红色')
# apple.info()

'''方法的继承'''
'''子类会重写父类的方法，对之类进行实例化后 子类调用的方法 执行的方法是子类的方法
	单个类继承的原则 子类继承了父类 但是子类没有重写父类的方法 那么子类实例化后的方法是子类当中的方法
'''
# class Fruit(object):
#
# 	def eat(self):
# 		print('keyichi')
#
# class Apple(Fruit):
# 	def __init__(self,color):
# 		self.__color=color
#
# 	def eat(self):
# 		print('颜色是红来吃')
#
# # apple=Apple('红色')
# # apple.eat()
#
# class UsaApple(Apple):
# 	def eat(self):
# 		print('woshimeiguode1pg')
#
# usa=UsaApple('红色')
# usa.eat()

class People(object):
	def __init__(self,name):
		self.name=name

	def info(self):
		print(self.name)
#当子类和父类有不同的实例属性时需要重写构造函数
# class Son(Person):
# 	def __init__(self,name,age,address):
# 		self.name=name
# 		#Person.__init__(self,name)
# 		self.age=age
# 		self.address=address
#
#
# 	def info(self):
# 		print(self.name)
#
# s=Son('hxj','11','sss')
# #s=Son('hxj')
# s.info()

'''
多个类的继承 从左到右的原则
'''

class Person(object):
	def eat(self):
		print('chifanle')

class Monther(Person):
	def eat(self):
		print('chicai')

class Father(Person):
	def eat(self):
		print('chishuiguo')

# class Son(Monther,Father):#从左到右
# 	pass

class Son(Monther,Person):#这n个类必须同一层级
	pass


son=Son()
son.eat()