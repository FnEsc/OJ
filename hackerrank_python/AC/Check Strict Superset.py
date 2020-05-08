s0=set(input().split())
r=True
for _ in range(int(input())):
    r=set(input().split()).issuperset(s0)
    if r==False:
        break
print(r)
# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))