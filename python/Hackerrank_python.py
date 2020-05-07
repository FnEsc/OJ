# -*- coding: UTF-8 -*-
# Author: h1033742389
# Date: 2019-09-11
# Email: smLin97@outlook.com
# Number of Questions: 115


#----------START Introduction----------#
#--->Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#--->Python If-Else
#!/bin/python3
N = int(input())
if N%2!=0:
    print("Weird")
elif 2<=N<=5:
    print("Not Weird")
elif 6<=N<=20:
    print("Weird")
else:
    print("Not Weird")

#--->Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#--->Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#--->Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#--->Write a function
def is_leap(year):
     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())
print(is_leap(year))

#--->Print Function
if __name__ == '__main__':
    n = int(input())
    t=""
    for i in range(1,n+1):
        t+=str(i)
    print(t)

#----------END Introduction----------#


#----------START Basic Data Types----------#
#--->List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = []
    p = 0
    for i in range ( x + 1 ) :
        for j in range( y + 1):
            for k in range(z+1):
                if i+j+k != n:
                    ar.append([])
                    ar[p] = [ i , j , k ]
                    p+=1
    print(ar)

#--->Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

#--->Nested Lists
if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] # 得到第二个分数

    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

#--->Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr=student_marks[query_name]
    print("%0.2f" % (float(sum(arr))/3))

#--->Lists
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

#--->Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

#----------END Basic Data Types----------#


#----------START Strings----------#
#--->sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#--->String Split and Join
def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#--->What's Your Name?
def print_full_name(firstname, lastname):
    print("Hello %s %s! You just delved into python." % (firstname,lastname))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#--->Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#--->Find a string
import re
def count_substring(string, sub_string):
    return len(re.findall(r'(?='+sub_string+')',string))
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#--->String Validators
if __name__ == '__main__':
    s = input()
    import re
    print(bool(re.findall(r'[0-9a-zA-Z]',s)))
    print(bool(re.findall(r'[a-zA-Z]',s)))
    print(bool(re.findall(r'[0-9]',s)))
    print(bool(re.findall(r'[a-z]',s)))
    print(bool(re.findall(r'[A-Z]',s)))

#--->Text Alignment
#Replace all ______ with rjust, ljust or center.
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#--->Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(" ".join(textwrap.wrap(string,max_width)),max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#--->Designer Door Mat
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

#--->String Formatting
def print_formatted(n):
    # your code goes here
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#--->Alphabet Rangoli
def print_rangoli(n):
    # your code goes here
    import string
    pattern_str=list(string.ascii_lowercase[:n])
    L=[]
    for i in range(n):
        s="-".join(pattern_str[i:n])
        L.append((s[::-1]+s[1::]).center(4*n-3,"-"))
    print("\n".join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#--->Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

#--->Complete the solve function below.
def solve(s):
    for x in s.split():
        s=s.replace(x,x.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

#--->The Minion Game
def minion_game(string):
    # your code goes here
    aeiou_sub_sum,qwer_sub_sum=0,0
    for i in range(len(string)):
        if string[i] in list("AEIOU"):
            aeiou_sub_sum+=len(string)-i
        else:
            qwer_sub_sum+=len(string)-i

    if aeiou_sub_sum==qwer_sub_sum:
        print("Draw")
    elif aeiou_sub_sum>qwer_sub_sum:
        print("Kevin",aeiou_sub_sum)
    else:
        print("Stuart",qwer_sub_sum)

if __name__ == '__main__':
    s = input()
    minion_game(s)

#--->Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here、
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#----------END Strings----------#


#----------START Sets----------#
#--->Introduction to Sets
def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#--->No Idea!
import time
x=time.clock()
N,M=map(int,input().split())
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happiness=0
for i in range(N):
    # happiness+=array.count(A[i])
    # happiness-=array.count(B[i])
    happiness+=int(array[i] in A)
    happiness-=int(array[i] in B)
print(happiness)
# print(time.clock()-x)

# Symmetric Difference
# N=int(input())
# a=set(map(int,input().split()))
# M=int(input())
# b=set(map(int,input().split())) # 等价上4条
a,b = [set(input().split()) for _ in range(4)][1::2] # [x:y:n] : 从x到y-1，每n个取一个制作切片
c=list(map(str,(sorted(a.difference(b).union(b.difference(a)),key=int))))
print("\n".join(c))


#--->Set .add()
# N=int(input())
# s=set()
# for _ in range(N):
#    s.add(input())
# print(len(s))
print(len(set([input() for _ in range(int(input()))])))

#--->Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    arr=input().split()
    cmd=arr[0]
    if cmd=="pop":
        s.pop()
    else:
        eval("s.{0}({1})".format(cmd,arr[1]))
print(sum(s))

#---> Set .union() Operation
s1,s2=[set(input().split()) for _ in range(4)][1::2]
print(len(s1|s2))

#--->Set .intersection() Operation
s1,s2=[set(input().split()) for _ in range(4)][1::2]
print(len(s1&s2))

#--->Set .difference() Operation
s1,s2=[set(input().split()) for _ in range(4)][1::2]
print(len(s1-s2))

#--->Set .symmetric_difference() Operation
s1,s2=[set(input().split()) for _ in range(4)][1::2]
print(len(s1^s2))

#--->Set Mutations
N,A=[input(),set(input().split())]
for _ in range(int(input())):
    cmd=input().split()[0]
    args=set(input().split())
    eval("A.{0}({1})".format(cmd,args))
print(sum(map(int,A)))

#--->The Captain's Room
k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))

#--->Check Subset
for _ in range(int(input())):
    s1,s2=[set(input().split()) for _ in range(4)][1::2]
    print(s1.issubset(s2))

#--->Check Strict Superset
s0=set(input().split())
r=True
for _ in range(int(input())):
    r=s0>set(input().split())
    if r==False:
        break
print(r)
# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))

#----------END Sets----------#


#----------START Math----------#
#--->Polar Coordinates
import cmath
arr=input()
print(abs(complex(arr)))
print(cmath.phase(complex(arr)))

#--->Find Angle MBC
import math
AB,BC=[int(input()) for _ in range(2)]
AC=(AB**2+BC**2)**(1/2)
BM=AC/2
cosA=(BC**2)/(2*BM*BC)
print(str(round(math.degrees(math.acos(cosA))))+"°")

#--->Triangle Quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(pow((10**i-1)//9,2))

#--->Mod Divmod
a,b=[int(input()) for _ in range(2)]
print(a//b)
print(a%b)
print(divmod(a,b))

#--->Power - Mod Power
a,b,c=map(int,[input().split()[0] for _ in range(3)])
print(a**b)
print(pow(a,b,c))

#--->Integers Come In All Sizes
a,b,c,d=map(int,[input() for _ in range(4)])
print(a**b+c**d)

#--->Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(10**i//9*i)

#----------END Math----------#


#----------START Itertools----------#
#--->itertools.product()
import itertools
A,B=[[int(x) for x in input().split()] for _ in range(2)]
print(" ".join(map(str,itertools.product(A,B))))

#--->itertools.permutations()
import itertools
arr,N=[sorted(i) for i in input().split()]
print("\n".join(["".join((list(map(str,i)))) for i in list(itertools.permutations(arr,int(N[0])))]))

#--->itertools.combinations()
import itertools
arr,N=[sorted(i) for i in input().split()]
for i in range(1,int(N[0])+1):
    print("\n".join(list(["".join(i) for i in itertools.combinations(arr,i)])))

#--->itertools.combinations_with_replacement()
import itertools
arr,N=input().split()
for i in itertools.combinations_with_replacement(sorted(arr),int(N)):
    print("".join(i))

#--->Compress the String!
import itertools
print(*[(len(list(c)), int(k)) for k, c in itertools.groupby(input())])

#--->Iterables and Iterators
import itertools
m,lst,n=[input().split() for _ in range(3)]
lst_com=itertools.combinations(lst, int(n[0]))
go=0
total=0
for i in lst_com:
    total+=1
    if 'a' in i:
        go+=1
print(round(go/total,4))

#--->Maximize It!
import itertools
K,M=map(int,input().split())
lst=[]  # 保存所有输入数组中i**2后的值的数组
for _ in range(K):
    lst.append(list([int(x)**2 for x in input().split()[1:]]))
print(max([sum(i)%M for i in list(itertools.product(*lst))]))

#----------END Itertools----------#


#----------START Collections----------#
#--->collections.Counter()
import collections
N,arr,n=[[int(x) for x in input().split()] for _ in range(3)]
L=[]
for i in range(n[0]):
    L.append([int(x) for x in input().split()])
dic=collections.Counter(arr)
total=0
for i in L:
    if i[0] in dic.keys():
        if dic[i[0]]!=0:
            dic[i[0]]-=1
            total+=i[1]
print(total)

#--->DefaultDict Tutorialimport collections
n,m=map(int,input().split())
d=collections.defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(" ".join(map(str,(d[input()]))) or -1)

#--->Collections.namedtuple()
import collections
N,arr=[input() for _ in range(2)]
std=collections.namedtuple('std',arr)
print("%.2f" % (sum([float(i.MARKS) for i in [std(*tuple(input().split())) for _ in range(int(N))]])/int(N)))

#--->Collections.OrderedDict()
import collections
ordered_dictionary = collections.OrderedDict()
N=int(input())
for i in range(N):
    item, quantity = input().rsplit(None, 1)
    if item not in ordered_dictionary:
        ordered_dictionary[item]=int(quantity)
    else:
        ordered_dictionary[item]+=int(quantity)
for i in ordered_dictionary.items():
    print(*map(str,i))

#--->Word Order
import collections
ordered_dict=collections.OrderedDict()
for _ in range(int(input())):
    temp=input()
    if temp in ordered_dict.keys():
        ordered_dict[temp]+=1
    else:
        ordered_dict[temp]=1
    # ordered_dict[temp]+=1 if temp in ordered_dict.keys() else ordered_dict.update({temp:1})
print(len(ordered_dict))
print(*ordered_dict.values())

#--->Collections.deque()
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

#--->Company Logo
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
# Input (stdin):aabbbccde
# Expected Output:
# b 3
# a 2
# c 2

#--->Piling Up!
for _ in (range(int(input()))):
    l=int(input())
    i=0
    side_lengths = list(map(int, input().split()))
    while i<l-1 and side_lengths[i]>=side_lengths[i+1]:
        i+=1
    while i<l-1 and side_lengths[i]<=side_lengths[i+1]:
        i+=1
    print("Yes" if i==l-1 else "No")

#----------END Collections----------#


#----------START Date and Time----------#
#--->Calendar Module
import calendar
arr=list(map(int,input().split()))
print(list(calendar.day_name)[calendar.weekday(arr[2], arr[0], arr[1])].upper())

#--->Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    import datetime
    dtdemo="%a %d %b %Y %H:%M:%S %z"
    return str(int(abs((datetime.datetime.strptime(t1,dtdemo)-datetime.datetime.strptime(t2,dtdemo)).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

#----------END Date and Time----------#


#----------START Errors and Exceptions----------#
#--->Exceptions
def go(x,y):
    try:
        print(int(x)/int(y))
    except Exception as e:
        print ("Error Code:",str(e))
for i in range(int(input())):
    go(*tuple(input().split()))

#--->Incorrect Regex
import re
for _ in range(int(input())):
    try:
        pattern=re.compile(input())
        print(True)
    except:
        print(False)

#----------END Errors and Exceptions----------#


#----------START Classes----------#
#--->Classes: Dealing with Complex Numbers
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary,self.imaginary*no.real+self.real*no.imaginary)
    def __truediv__(self, no):
        a=self.real
        b=self.imaginary
        c=no.real
        d=no.imaginary
        div_real=(a*c+b*d)/(c**2+d**2)
        div_imaginary=(b*c-a*d)/(c**2+d**2)
        return Complex(div_real,div_imaginary)
    def mod(self):
        return Complex(math.sqrt(self.real**2+self.imaginary**2),0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

#--->Class 2 - Find the Torsional Angle
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return  Points((self.x-no.x),(self.y-no.y),(self.z-no.z))
    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)
    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))

#----------END Classes----------#


#----------END Built-Ins----------#
#--->Zipped!
N,M=map(int,input().split())
z=zip(*[input().split() for _ in range(M)])
for i in z:
    print(sum(map(float,i))/M)

#--->Input()
x,y=map(int,input().split())
s=input().replace("x",str(x))
print(True) if eval(s)==y else print(False)

#--->Python Evaluation
eval(input())

#--->Athlete Sort
import collections
N,M=map(int,input().split())
Man=collections.namedtuple('Mam',",".join(map(lambda x:"x"+str(x),range(M))))
# print(Man)
Mans=[Man(*tuple(map(int,input().split()))) for _ in range(N)]
# print(Mans)
sort_mans=sorted(Mans,key=eval("lambda x:x.x{}".format(input())))
for i in sort_mans:
    print(*i)

#--->Any or All
N,arr=[input().split() for _ in range(2)]
print(any([i==i[::-1] for i in arr]) and all([int(i)>0 for i in arr]))

#--->ginortS
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')

#----------END Built-Ins----------#


#----------END Python Functionals----------#
#--->Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 
def fibonacci_Yield_tool(n):
    a,b=0,1
    while n>0:
        yield b
        a,b=b,a+b
        n-=1

def fibonacci(n):
    # return a list of fibonacci numbers
    return ([0]+list(fibonacci_Yield_tool(n-1)))[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#--->Validating Email Addresses With a Filter
def fun(s):
    # return True if s is a valid email, else return False
    import re
    return bool(re.match(r"^[\w-]+@[0-9a-zA-Z]+\.+[a-zA-Z]{1,3}$",s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#--->Reduce Function
from fractions import Fraction
from functools import reduce

def product(fracs):
    t =reduce(lambda x, y : x * y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

#----------END Python Functionals----------#


#----------END Regex and Parsing----------#
#--->Detect Floating Point Number
import re
pattern=re.compile(r"^[+-]?[0-9]*\.[0-9]+$")
for _ in range(int(input())):
    print(bool(re.match(pattern,input())))

#--->Re.split()
import re
print("\n".join(map(str,re.split(r"[.,]+",input()))))

import re
print("\n".join(re.split(regex_pattern, input())))

#--->Group(), Groups() & Groupdict()
import re
m=re.search(r"([0-9a-zA-Z])\1+",input())
print(m.group(1) if m else -1)

#--->Re.findall() & Re.finditer()
import re
v="aeiou"
c="qwrtypsdfghjklzxcvbnm"
m=re.finditer(r"(?<=[%s])([%s]){2,}(?=[%s])" % (c,v,c),input(),flags=re.I)
print( ("\n".join(map(lambda x: x.group(),m))) or -1)

#--->Re.start() & Re.end()
import re
s,p=[input() for _ in range(2)]
m=re.finditer(r"(?=%s)"%p,s)
print("\n".join(map(str,[tuple([i.start(),i.start()+len(p)-1]) for i in m])) or (-1,-1))

#--->Regex Substitution
import re
pattern_and=re.compile(r"(?!(^#))(?<= )&&(?= )")
pattern_or=re.compile(r"(?!(^#))(?<= )\|\|(?= )")
for _ in range(int(input())):
    print(re.sub(pattern_or, "or",re.sub(pattern_and, "and", input())))

#--->Validating Roman Numerals
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern=thousand+hundred+ten+digit+"$"

import re
print(str(bool(re.match(regex_pattern, input()))))

#--->Validating phone numbers
import re
for _ in range(int(input())):
    print("YES") if bool(re.match(r"^[789][0-9]{9}$",input())) else print("NO")

#--->Validating and Parsing Email Addresses
import re
for _ in range(int(input())):
    x,y=input().split()
    m=re.match(r"^<[a-zA-Z](\w|\.|-)*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$",y)
    print(x,y) if m else None

#--->Hex Color Code
import re
for _ in range(int(input())):
    m=re.findall(r"(?<!^)#(?:[a-fA-F0-9]{3}){1,2}",input())
    print("\n".join(m)) if m else None

#--->HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

    def handle_endtag(self, tag):
        print ('End   :',tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

#--->HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#--->Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

#--->Validating UID
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

#--->Validating Credit Card Numbers
import re
pattern=re.compile(r"^" r"(?!.*(\d)(-?\1){3})" r"([456]\d{3})(-?\d{4}){3}$")
for _ in range(int(input())):
    m=re.match(pattern,input())
    print("Valid" if m else "Invalid")

#--->Validating Postal Codes
regex_integer_in_range = r"^[1-9]\d{5}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r".*(?=(\d).\1)"  # Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#--->Matrix Script
import re
n,m = map(int,input().split())
matrix = []
s = ''
for line in range(n):
    matrix.append(input()+' ')
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
s1 = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',s)
print(s1)

#----------END Regex and Parsing----------#


#----------START XML----------#
#--->XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node): # 这里是递归的了
  return len(node.attrib) + sum(get_attr_number(child) for child in node)
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#--->XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#----------END XML----------#


#----------END Closures and Decorators----------#
#--->Standardize Mobile Number Using Decorators
def wrapper(function1):
    def fun0(l):
        # complete the function
        function1(["+91 "+i[-10:-5]+" "+i[-5:] for i in l])
    return fun0

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

#--->Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
# 注释：
# @decorator
#  def somefunction(secs)
#  python解析器遇到@，且后面跟着函数时，会把函数somefunction当做参数传递给decorator函数并执行，即decorator(somefunction)

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


#----------END Closures and Decorators----------#


#----------START Numpy----------#
#--->Arrays
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#--->Shape and Reshape
import numpy
my_array = numpy.array(input().split(),int)
print(numpy.reshape(my_array,(3,3)))

#--->Transpose and Flatten
import numpy
N,M=input().split()
my_array = numpy.array([input().split() for _ in range(int(N))],int)
print(numpy.transpose(my_array))
print(my_array.flatten())

#--->Concatenate
import numpy
N,M,P=input().split()
array_1 = numpy.array([input().split() for _ in range(int(N))],int)
array_2 = numpy.array([input().split() for _ in range(int(M))],int)
print(numpy.concatenate((array_1, array_2)))

#--->Zeros and Ones
import numpy
nums=tuple(map(int,input().split()))
print(numpy.zeros(nums, dtype = numpy.int)) # 维度,行,列
print(numpy.ones(nums, dtype = numpy.int)) # 维度,行,列

#--->Eye and Identity
import numpy
numpy.set_printoptions(sign=' ')
# N,M=map(int,input().split())
print(numpy.eye(*map(int,input().split())))
# print(numpy.eye(*[3,3]))

#--->Array Mathematics
import numpy
N,M=tuple(map(int,input().split()))
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)
print(numpy.add(A,B)) # +
print(numpy.subtract(A,B)) # -
print(numpy.multiply(A,B)) # *
print(A//B) # //
print(numpy.mod(A,B)) # %
print(numpy.power(A,B)) # **

#--->Floor, Ceil and Rint
import numpy
numpy.set_printoptions(sign=' ')
my_array=numpy.array(list(map(float,input().split())))
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

#--->Sum and Prod
import numpy
N,M=tuple(map(int,input().split()))
my_array=numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(my_array, axis = 0), axis = None))

#--->Min and Max
import numpy
N,M=tuple(map(int,input().split()))
my_array=numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(my_array, axis = 1),axis=None))

#--->Mean, Var, and Std
import numpy
numpy.set_printoptions(sign=' ')
N,M=tuple(map(int,input().split()))
my_array = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),12))

#--->Dot and Cross
import numpy
n=int(input())
A = numpy.array([input().split() for _ in range(n)],int)
B = numpy.array([input().split() for _ in range(n)],int)
print(numpy.dot(A,B))

#--->Inner and Outer
import numpy
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))

#--->Polynomials
import numpy
print(numpy.polyval(list(map(float,input().split())), int(input())))

#--->Linear Algebra
import numpy
N=int(input())
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(N)])),2))

#----------END Numpy----------#


#----------START Debugging----------#
#--->Words Score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))

#--->Default Arguments
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

#----------END Debugging----------#



