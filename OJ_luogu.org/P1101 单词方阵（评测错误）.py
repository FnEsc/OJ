# -*- coding: utf-8 -*-
n = int(input())
nn=[]
for i in range(n):
    nn.append(input())
allstr=[]
stay=[]

# 向右
for i in range(n):
    for j in range(n-6):
        allstr.append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
# 向下
for j in range(n):
    for i in range(n-6):
        allstr.append([[i,j],[i+1,j],[i+2,j],[i+3,j],[i+4,j],[i+5,j],[i+6,j]])
# 向右下
for i in range(n-6):
    for j in range(n-6):
        allstr.append([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3],[i+4,j+4],[i+5,j+5],[i+6,j+6]])
# 向右上
for i in range(6,n-1):
    for j in range(6,n-1):
        allstr.append([[i,j],[i-1,j-1],[i-2,j-2],[i-3,j-3],[i-4,j-4],[i-5,j-5],[i-6,j-6]])

for a in allstr: # a为一串
    temp=nn[a[0][0]][a[0][1]]+nn[a[1][0]][a[1][1]]+nn[a[2][0]][a[2][1]]+nn[a[3][0]][a[3][1]]+nn[a[4][0]][a[4][1]]+nn[a[5][0]][a[5][1]]+nn[a[6][0]][a[6][1]]
    if temp=="yizhong" or temp=="gnohziy" :
        # stay.append(a[0]).append(a[1]).append(a[2]).append(a[3]).append(a[4]).append(a[5]).append(a[6])
        stay.extend(a)
for i in range(n):
    for j in range(n):
        if [i,j] not in stay:
            temp_s=list(nn[i])
            temp_s[j]="*"
            nn[i]="".join(temp_s)
    print(nn[i])

