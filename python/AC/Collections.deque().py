import collections
d=collections.deque()
for _ in range(int(input())):
    arr=input().split()
    if len(arr)==1:
        cmd=arr[0]
        eval("d.{0}()".format(cmd))
    else :
        cmd,args=arr[0],*arr[1:]
        eval("d.{0}({1})".format(cmd,args))
print(" ".join(map(str,d)))