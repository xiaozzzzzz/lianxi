'''
集合
集合中数据无序，不可使用索引，分片
集合中数据具有唯一性，可以用来排除重复数据
集合内的数据，str, int float, tuple,即内部只能放置可哈希数据
'''

s = set()
print(type(s))

s = {1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

d = {}
print(type(d))

s1 = {2, 3, 4, "i", "love", "you"}
for i in s1:
	print(i, end="\t")
print("\t")

s2 = {(1, 2, 3), ("i", "lobe", "you"), (4, 5, 6)}
print(s2)

s2.add(8)												# add可以添加数据
print(s2)

s2.discard(8)											# discard可以删除指定数据（和remove一样）
print(s2)

s2.pop()												# pop随机移除了一组数据
print(s2)

s2.clear()												# clear 是清空数据
print(s2)

s = {2, 3, 4}
s3 = s1.intersection(s)									# 交集
s4 = s1.difference(s)									# 差集
s5 = s1.union(s)										# 并集
s6 = s1.issubset(s)										# 检查是否为子集
s7 = s1.issuperset(s)									# 检查是否为超集

print(s)
print(s1)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

s0 = frozenset()										# 冰冻集合，即不可更改
print(type(s0))