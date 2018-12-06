l1 = [1, 2, 3, 4, 5, 7, 10, 15, 2, 9, 10]
print(l1)
for i in range(len(l1)):  # 修改list集合的数据
    if(i%2 ==1):
        l1[i] = 0
print(l1)
print(l1[0:len(l1)])
print(l1[0:len(l1):2])    # 最后的2是隔2-1打一个
print(l1[-4:-2])          # 负数当下标也是可以的，但是左边的下标必须小与右边的
print(l1[-1:-6:-1])       # 除非最后一个间距为负数
print(id(l1[1]))          # id是确定数据的唯一编号
c = l1[1]
print(id(c))              # 赋值的过程中没有重新生成一个数据

g_length = l1.count(0)      # count 是查找并返回指定值的个数
print(g_length)

del l1[2:9]
print(l1)
l1.remove(1)              # remove del 均为删除
print(l1)

w = [i*10 for i in l1]      # list内涵
print(w)

l2 = l1[2:3]

l = l1+l2                   # list可以相加
print(l)

for i in range(len(l)):
    print(l[i], end='\t')

h=["I love you"]
for i in h:
    print(i)

sna = [[1, 54, "wqdwq"], [3, "w", "dwqud"], [9, 42, "wqdwq"]]   # 和c语言的数组一样,
for i in range(0, 3):
    for j in range(0, 3):
        print(sna[i][j],end='\t ')                              # print 里面的end表示换行的格式
help(print)                                                     # help函数是查找帮助

wj = [i for i in range(100, 1000) if i % 100 == 0]              # 列表可以嵌套
print(wj)
wj.append(10)               # append在列表中添加数据，默认位置为列表最后
print(wj)
wj.insert(6, 100)            # insert里面的第一个是位置，第二个是数据
print(wj)

print(list(range(0, 10)))   # 用列表打印出0-9的数

a1 = "1,2,3"                  # 将a1以列表的形式打印
print(list(a1))

c1 = l1.copy()                # 复制列表要用copy
print(c1)
