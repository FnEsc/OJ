def go(x,y):
    try:
        print(int(x)/int(y))
    except Exception as e:
        print ("Error Code:",str(e))
for i in range(int(input())):
    go(*tuple(input().split()))