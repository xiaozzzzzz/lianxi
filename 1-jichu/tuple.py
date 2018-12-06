'''
元组
元组除了可修改都可以
'''


t = ()
print(type(t))
t = (1)
print(type(t))
print(t)
t = (1, 2, 3, 4, 5)
print(type(t))
print(t)
t = 1, 2, 3, 4, 5			# 元组定义时可以不用括号
print(t)
print(t[1])
print(t[0:5])				# 输出时上限可以超出范围，但不可直接输出超过上限的元组
							# print(t[10])
t1 = 1, 2, 3, 4
t2 = t1 + t					# 元组可以相加，输出跟list一样
print(t2)
for i in range(len(t)):
	print(t[i], end='\t')
t3 = ((1, 2, 3), ("wdqwd", 2, 4))
print(t3[1][2])

print(max(t))				# 可以用max直接输出元组的最大值，min同理
l = list(t)
print(l)					# 可以用强制转换符号把元组转换成列表，其他同理
print(l.index(3))			# 可以用index查找指定数据出现的位置