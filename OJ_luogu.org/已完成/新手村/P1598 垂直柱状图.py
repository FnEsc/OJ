# -*- coding: utf-8 -*-
import string
art = ""
for i in range(4):
    art += input().replace(" ","")

count_list = []
for i in string.ascii_uppercase :
    count_list.append(art.count(i))

count_max = max(count_list)
for i in range(count_max):
    # 当前行输出星号
    this_line = []
    k = 0 # k为记录应该输出到达哪列
    for j in range(26):
        if count_list[j] >= (count_max-i):
            this_line.append("*")
            k = j
        else :
            this_line.append(" ")
        # 记住每行的最后的*在哪个位置，之后不再输出
    print(" ".join(this_line[:k+1]))

print(" ".join(string.ascii_uppercase))