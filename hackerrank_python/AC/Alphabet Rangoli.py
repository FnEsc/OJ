import string
n=int(input())
pattern_str=list(string.ascii_lowercase[:n])
L=[]
for i in range(n):
    s="-".join(pattern_str[i:n])
    L.append((s[::-1]+s[1::]).center(4*n-3,"-"))
print("\n".join(L[:0:-1]+L))