# -*- coding: utf -8 -*-

str0 = input()
new = []
if str0.find(".") != -1 :
    list0 = str0.split(".")
    for x in list0 :
        new.append(str(int(str(int(x))[::-1])))
    print(".".join(new))
elif str0.find("/") != -1 :
    list0 = str0.split("/")
    for x in list0 :
        new.append(str(int(x[::-1])))
    print("/".join(new))
elif str0.find("%") != -1 :
    str0 = str(int(str0[-2::-1]))
    print(str0+"%")
else :
    print(int(str0[::-1]))