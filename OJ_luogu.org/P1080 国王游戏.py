# 注意题解！
n=int(input())
[A,B]=[int(x) for x in input().split()]
sort_ab=[]
for i in range(n):
    [a,b]=[int(x) for x in input().split()]
    sort_ab.append([a,b,a*b])
sort_ab=sorted(sort_ab,key=lambda x:x[2])
temp=A
the_less_gets=[]
for i in range(n):
    the_less_gets.append(temp/sort_ab[i][1])
    temp*=sort_ab[i][0]
print(int(max(the_less_gets)))