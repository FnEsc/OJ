if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range(N):
        temp=input().split()
        cmd=temp[0]
        args = temp[1:]
        eval('arr.{0}{1}'.format(cmd,tuple(map(int,args)))) if temp[0]!='print' else print(arr)
        # if temp[0]=='print':
        #     print(arr)
        # elif temp[0]=='insert':
        #     arr.insert(int(temp[1]),int(temp[2]))
        # elif temp[0]=='remove':
        #     arr.remove(int(temp[1]))
        # elif temp[0]=='pop':
        #     arr.pop()
        # elif temp[0]=='sort':
        #     arr.sort()
        # elif temp[0]=='reverse':
        #     arr.reverse()
        # elif temp[0]=='append':
        #     arr.append(int(temp[1]))
