import sys
sys.setrecursionlimit(1000000)
n=int(input())
total=0 # 总解数
sum_pr=0 # 统计输出解
temp_c=[x for x in range(n)] # 存放临时解
def dsf(queen):
    global total
    global temp_c
    global sum_pr
    if queen==n: # 如果走到了这,所以皇后一定不会冲突
        total+=1
        sum_pr+=1
        if (sum_pr<=3):
            print(" ".join([str(x+1) for x in temp_c]))
    else:
        for i in range(n): # 列开始排,行排下去
            ok=1 # 标志合法
            temp_c[queen]=i # 第queen个皇后放在第i列,这是尝试
            for j in range(queen): # 已放置queen个皇后,逐个检查与第j个皇后是否合法
                if ( (temp_c[queen]==temp_c[j]) or (queen-temp_c[queen]==j-temp_c[j]) or (queen+temp_c[queen]==j+temp_c[j]) ): # 列重复、反斜杠重复、斜杠重复
                    ok=0 # 冲突
                    break
            if (ok):
                dsf(queen+1)
dsf(0)
print(total)