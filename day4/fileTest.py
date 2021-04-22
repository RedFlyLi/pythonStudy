#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ

'''
open()函数的参数:
1.要操作的文件名称
2.以什么样的方式操作文件
r:只读模式
w:只写模式【不可读 不存在就创建 存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a:增加模式【可读，不存在就创建，存在只增加内容】
"+"表示可以同时读写某个文件，具体为：

r+：读写
w+：写读
x+：写读
a+：写读
'''
#写文件
# f=open('file.login','w')
# temp={
# 	"name":"hxj",
# 	"age":20,
# 	"address":"xian"
# }
# f.writelines(temp)
# f.close()
# 追加
# import login
# login.dump(temp,open('file.login','w'))
#
# f=open('file.login','a')
# f.write('adbbbb')
# f.close()
#覆盖
# f=open('file.login','w')
# f.write('fugai')
# f.close()

#读
f=open('file.login','r')
#read()读取文件的所有内容
#print(f.read())

#readlines()读取文件的行数 默认读取文件的第一行
#print(f.readlines())

# for i in f.readlines():
# 	print(i)

#读几个只读取文件中几个
print(f.read(7))

'''文件的上下文的处理'''
with open('file.login','w') as f:
	f.write('wuya')
'''自动帮助处理close()'''