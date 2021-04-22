#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:HXJ



# try:
# 	div(1, 0)
# except ZeroDivisionError as e:
# 	print(e.args)
'''
1、try代码执行正常，就不会执行expect的代码
2、只有try代码执行异常，才会执行expect的代码
'''


def div(a, b):
	return a / b
try:
	# div(1, 0)
	#div(1, 'srg')
	div(1,{'wda':'fda'})
# except KeyError as e:
# 	print(e.args)
# except ValueError as e:
# 	print(e.args)
# except ZeroDivisionError as e:
# 	print(e.args)
# except WindowsError as e:
# 	print(e.args)
except Exception as e:
	print(e.args)

'''
try--expect--else--finally
先执行try 如果执行通过 就执行else代码 最后执行finally
如果try执行失败 就直接执行finally
'''

try:
	div(1,1)
except Exception as e:
	pass
else:
	print('pass')
finally:
	print('fianlly')
