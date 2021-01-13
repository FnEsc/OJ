# -*- coding: utf-8 -*-
n=int(input())

go=[]
# n表示总味道,t表示未下的味道数
if 10<=n<=30:
    for i1 in range(1,4):
        for i2 in range(1,4):
            for i3 in range(1,4):
                for i4 in range(1,4):
                    for i5 in range(1,4):
                        for i6 in range(1,4):
                            for i7 in range(1,4):
                                for i8 in range(1,4):
                                    for i9 in range(1,4):
                                        for i10 in range(1,4):
                                            if (i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)==n:
                                                go.append([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10])
    print(len(go))
    for i in go:
        print(" ".join(str(j) for j in i))
else:
    print("0")