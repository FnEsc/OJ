# -*- coding: utf-8 -*-

w_dict={}
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)
    elif a<b and b<c :
        # 参数1
        if ("[%d,%d,%d]"%(a,b,c-1)) in w_dict.keys():
            temp_1=w_dict.get(("[%d,%d,%d]"%(a,b,c-1)))
        else:
            temp_1=w(a,b,c-1)
            w_dict.update({("[%d,%d,%d]"%(a,b,c-1)):temp_1})
        # 参数2
        if ("[%d,%d,%d]"%(a,b-1,c-1)) in w_dict.keys():
            temp_2=w_dict.get("[%d,%d,%d]"%(a,b-1,c-1))
        else:
            temp_2=w(a,b-1,c-1)
            w_dict.update({("[%d,%d,%d]"%(a,b-1,c-1)):temp_2})
        # 参数3
        if ("[%d,%d,%d]"%(a,b-1,c)) in w_dict.keys():
            temp_3=w_dict.get("[%d,%d,%d]"%(a,b-1,c))
        else:
            temp_3=w(a,b-1,c)
            w_dict.update({("[%d,%d,%d]"%(a,b-1,c)):temp_3})
        return temp_1+temp_2-temp_3
    else:
        # 参数1
        if ("[%d,%d,%d]"%(a-1,b,c)) in w_dict.keys():
            temp_1=w_dict.get("[%d,%d,%d]"%(a-1,b,c))
        else:
            temp_1=w(a-1,b,c)
            w_dict.update({("[%d,%d,%d]"%(a-1,b,c)):temp_1})
        # 参数2
        if ("[%d,%d,%d]"%(a-1,b-1,c)) in w_dict.keys():
            temp_2=w_dict.get("[%d,%d,%d]"%(a-1,b-1,c))
        else:
            temp_2=w(a-1,b-1,c)
            w_dict.update({("[%d,%d,%d]"%(a-1,b-1,c)):temp_2})
        # 参数3
        if ("[%d,%d,%d]"%(a-1,b,c-1)) in w_dict.keys():
            temp_3=w_dict.get("[%d,%d,%d]"%(a-1,b,c-1))
        else:
            temp_3=w(a-1,b,c-1)
            w_dict.update({("[%d,%d,%d]"%(a-1,b,c-1)):temp_3})
        # 参数4
        if ("[%d,%d,%d]"%(a-1,b-1,c-1)) in w_dict.keys():
            temp_4=w_dict.get("[%d,%d,%d]"%(a-1,b-1,c-1))
        else:
            temp_4=w(a-1,b-1,c-1)
            w_dict.update({("[%d,%d,%d]"%(a-1,b-1,c-1)):temp_4})
        return temp_1+temp_2+temp_3-temp_4

while 1:
    [a,b,c]=[int(x) for x in input().split()]
    if a==b==c==-1:
        break
    if ("[%d,%d,%d]"%(a,b,c)) in w_dict.keys():
        temp_num=w_dict.get("[%d,%d,%d]"%(a,b,c))
    else:
        temp_num=w(a,b,c)
        w_dict.update({("[%d,%d,%d]"%(a,b,c)):temp_num})
    print("w(%d, %d, %d) = %d" % (a,b,c,temp_num))