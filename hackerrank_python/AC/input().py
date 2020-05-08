x,y=map(int,input().split())
s=input().replace("x",str(x))
print(True) if eval(s)==y else print(False)