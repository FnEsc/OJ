# -*- coding: utf-8 -*-

# 题目分析
# 因为士兵掉头之后会交换坐标，等价于两人交换，但坐标在质量上是没有改变的，因此可以看做士兵继续行走

L = input()# "请输入一个整数L，表示独木桥的长度："
L = int(L)
N = input()# "请输入一个整数N，表示初始留在桥上的士兵目数："
N = int(N)
if N==0 :
	print("0 0")
else :
	list0 = input().split()# list0代表输入的士兵坐标
	list1 = list0.copy()# 为了不破坏原数据，临时浅复制给变量list2
	list2 = list(set(list1))  #使用set()函数将list2转为集合去掉重复元素又用list()转回list2<string>
	# list2转为list<int>
	list2 = [ int(i) for i in list2 ]
	list2.sort()
	# list2为不重复的士兵坐标，并从小到大排列
	# print(list2)

	l = len(list2)# l代表士兵个数

	# 判断士兵个数是否与预设相等
	if (l!=N) :
		#print("输入有误，请重新运行程序！")
		#assert l != N
		print("0 0")
	else :
		# 判断是否符合逻辑
		if (0<N<=L<=5000)!= 1 :
			#print("输入有误，请重新运行程序！")
			#assert (0<N<=L<=5000)!=1
			print("0 0")
		else :
			# 分3层，min0,midmin0,midmax0,max0
			min0 = list2[0]
			max0 = list2[l-1]

			midmid = []
			midmin = []
			midmax = []

			# LL定义为取L的偶数
			if L%2 == 0 :
				LL = L
			else :
				LL = L+1

			# 靠中距离组成list
			for index in range(l) :
				if L%2 == 0 :
					# 取最靠近中距离
					midmid0 = min(abs(list2[index]-LL/2),abs(list2[index]-(LL/2)-1))
					midmid.append(midmid0)
				else :
					midmid0 = abs(list2[index]-LL/2)
					midmid.append(midmid0)

			# midmid为坐标距中间距离
			# print(midmid)
			# 开始最短时间，为最靠近中间的人向最近的方向跑
			midmid.sort()
			midmin0 = midmid[0]
			shorttime = LL/2-midmin0
			# print(shorttime)

			# 开始判断最长时间，为最远中间的人向中间走，并应到达中点或（终点+1处即越过中点）再走向另一边
			midmax = midmid.copy()
			midmax.sort(reverse=True)
			midmax0 = midmax[0]
			# print(midmax0)
			longtime = midmax0+LL/2

			if L%2 == 0 :
				longtime+=1

			print(int(shorttime),int(longtime))