# -*- coding: utf-8 -*-
class Queue(object):
    """docstring for Queue"""
    # 初始化队列为空队列
    def __init__(self,m):
        self.items = []
        m=m
    def enqueue(self,item):
        self.items.append(item)
        # 控制此队列最长为3
        if len(self.items)>m:
            self.items.pop(0)
    def if_it_in(self,i):
        if i in self.items:
            return 0
        else:
            self.enqueue(i)
            return 1

[m,n]=[int(x) for x in input().split()]
page_list=[int(x) for x in input().split()]
q=Queue(m)
total=0
for i in page_list:
    total+=q.if_it_in(i)
print(total)