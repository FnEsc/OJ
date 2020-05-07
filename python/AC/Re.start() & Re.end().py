import re
s,p=[input() for _ in range(2)]
m=re.finditer(r"(?=%s)"%p,s)
print("\n".join(map(str,[tuple([i.start(),i.start()+len(p)-1]) for i in m])) or (-1,-1))