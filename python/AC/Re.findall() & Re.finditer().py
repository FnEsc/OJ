import re
v="aeiou"
c="qwrtypsdfghjklzxcvbnm"
m=re.finditer(r"(?<=[%s])([%s]){2,}(?=[%s])" % (c,v,c),input(),flags=re.I)
print( ("\n".join(map(lambda x: x.group(),m))) or -1)