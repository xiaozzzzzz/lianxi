'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student( ):
	# 一个空的类，pass代表直接跳过
	# 此处pass必须有
	pass

# 定义一个对象
class PythonStudent( ):
	# 用None给不确定的值赋值
	name = None
	age = 18
	course = "Python"
	
	# 需要注意
	# 1.def doHomework的缩进层次
	# 2.系统默认有一个self参数
	def doHomework(self):
		print("I 在做作业")
		
		# 推荐在函数末尾使用return语句
		return None

# 实体化一个wxz的学生
wxz = PythonStudent()
print(wxz.name)
print(wxz.age)
# 需要成员函数的调用没有传递进入参数
wxz.doHomework()
print(wxz)