# -*- coding: utf-8 -*-
flag=0
miwen=input().replace(' ','')
yuanwen=input().replace(' ','')
need=input().replace(' ','')
dictgo={}    # 原文对应密文

# 原文set长度为26
# 循环密文检查明文是否重复
# 密文set长度为26

for i in range(len(miwen)):
    if miwen[i] not in dictgo.values():# 密文第一次出现
        if yuanwen[i] not in dictgo.keys():
            dictgo.update({yuanwen[i]:miwen[i]})
        else:
            flag=1
            break
    else:# 密文出现过
        if miwen[i]==dictgo.get(yuanwen[i]):
            pass
        else:
            flag=1
            break

if len(dictgo.keys())!=26 or len(dictgo.values())!=26 :
    flag=1

if flag==1:
    print("Failed")
else:
    go=''
    dictback={v : k for k, v in dictgo.items()}
    for i in need:
        go+=dictback.get(i)
    print(go)
