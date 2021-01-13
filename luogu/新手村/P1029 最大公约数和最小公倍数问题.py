# -*- coding: utf-8 -*-


# 定义x0,y0
# 求P,Q对数

x0,y0 = input().split()
x0 = int(x0)
y0 = int(y0)

# k为P、Q的对数
k = 0


# 判断x0和y0的最大公约数得xy
# xy = 1
# i = 1
#print(xy)
#print(type(xy))
# while i<=x0 :
	#if (((x0%xy)==0) and ((y0%xy)==0)) :
	#print(xy)
	# if (    (x0%i==0) and (y0%i==0)     ) :
		# xy = i
		#xy = int(xy)
		#print("x0  y0=",x0,y0)
		#print(xy)
	#print("++++++++++")
	# i += 1


if ((2<=x0<100000)and(2<=y0<=1000000)) != 1 :
	k = 0
else :
	P = x0
	while (P<=y0) :
		# 判断P是否符合是否为整数
		#print(P)
		if y0%P == 0 :
			Q = (x0*y0)/P
			#print(P,Q)
			# 且y0能否整除Q
			if (y0%P==0) :
				# 判断P和Q的最大公约数得PQ
				PQ = 1
				i = 1
				#print(P)
				#print(Q)
				while i<=P :
					if ((P%i==0) and (Q%i==0)) :
						PQ = i
						#print("---------------")
					i += 1
				if PQ == x0 :
					#print("PQ的最大公约数为",PQ,"符合条件的P,Q为",P,Q)
					#print("符合条件的P,Q为",P,Q)
					k += 1
		P += 1


print(k)
