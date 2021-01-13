# -*- coding: utf-8 -*-
n=int(input())
xs=[]
jj=[]
for i in range(n):
    [a,b,c,d,e,f]=input().split()   # a姓名 b期末平均成绩 c班级评议成绩 d是否是学生干部 e是否是西部省份学生 f以及发表的论文数
    xs.append([a,b,c,d,e,f])
for i in range(n):
    temp_jj=0
    if (int(xs[i][1])>80) & (int(xs[i][5])>=1) :
        temp_jj+=8000
    if (int(xs[i][1])>85) & (int(xs[i][2])>80) :
        temp_jj+=4000
    if int(xs[i][1])>90 :
        temp_jj+=2000
    if xs[i][4]=='Y' :
        if int(xs[i][1])>85 :
            temp_jj+=1000
    if int(xs[i][2])>80 :
        if xs[i][3]=='Y' :
            temp_jj+=850
    jj.append(temp_jj)

top=max(jj)
index=jj.index(top)
print(xs[index][0])
print(top)
print(sum(jj))
