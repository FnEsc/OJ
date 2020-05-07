import textwrap
s = input()
w = int(input())
l = " ".join(textwrap.wrap(s,w))
print(textwrap.fill(l,w))