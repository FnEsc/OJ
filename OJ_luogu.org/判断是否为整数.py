x = '1'
y = x.isdigit()
print(y)

# isdigit() 方法检测字符串是否只由数字组成。无法判断知否整数

y0 = 60
Q = 27
# 判断Q是否为整数且y0能否整除Q
#if ( 'Q'.isdigit() and ((y0%Q)==0) ) :
print('1asd'.isdigit())
print(y0%Q)

i = 0
while i<=10 :
	if i == 2 :
		xy = i
		print("break在if内层对循环while有用")
		break
	#print("break在if内层对循环while无用，事实上有用")
	i += 1
print(xy)