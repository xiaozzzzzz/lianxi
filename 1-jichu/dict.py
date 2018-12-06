'''
dict
字典
'''

d = {}
print(d)
d = dict()
print(d)

d = {"one": 1, "two": 2, "three": 3}
'''
创建有值的字典，每一组数据用冒号隔开，
每一对键值用逗号隔开
'''
print(d)
for i in d:
	print(i)

d = dict({"one": 1, "two": 2, "three": 3})			# 使用dict创建字典
print(d)

d = dict([("one", 1), ("two", 2), ("three", 3)])
print(d)

# 字典是序列类型，但是是无序序列，所以没有分片和索引
# 字典中的数据都有键值对组成，即kv对
# key:必须是可哈希值，比如：int,string,float,tuple,但是list,set,dict不行
# value:任何值
d1 = {"one": 1, "two": 2, "three": 3}
print(d["one"])
d1["one"] = "four"
print(d1)
del(d1["one"])
print(d1)

# 成员检测检测的是key
if 2 in d1:
	print("value")
if "two" in d1:
	print("key")
if ("two", 2) in d1:
	print("kv")
	
for k in d:
	print(k, d[k])		# 使用循环访问访问的是key
for k in d.keys():
	print(k, d[k])
for v in d.values():
	print(v)
for k, v in d.items():
	print(k, ' -->', v)
	
# 通用函数 len,max,min,dict
# str(字典),返回字典的字符串可是
print(str(d))

# clear:清空字典
# items:返回字典的键值对组成的元组格式
i = d.items()
print(type(i))
print(i)

# keys:返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)

# value:返回字典的valve组成的结构
v = d.values()
print(type(v))
print(v)

# get:根据指定的key返回相对应的值，且不会报错
print(d.get("two"))

# fromkeys:使用指定的序列作为键，使用一个值作为字典的所有键的值
d2 = ["ein", "zwe", "dre"]
d3 = dict.fromkeys(d2, "hahahahaha")
print(d3)