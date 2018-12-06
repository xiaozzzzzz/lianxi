'''
	n=1	A----->C
	
	n=2	A----->B	A----->C	B----->C
	
	n=3 A----->C	A----->B	C----->B	A----->C	B----->A	B----->C	A----->C
		借助C上面的两个盘子调到B上去，之后在借助A移到C上去
	m>4
		借助C移到B，之后借助A移到C，
'''

def hanoi (n,a,b,c):
	if(n==1):
		print(a,"---->",c)
	if(n==2):
		print(a,"---->",b)
		print(a,"---->",c)
		print(b,"---->",c)
	else:
		hanoi(n-1,a,c,b)
		print(a,"---->",c)
		hanoi(n-1,b,a,c)

n = 4
a="A"
b="B"
c="C"
hanoi(n,a,b,c)