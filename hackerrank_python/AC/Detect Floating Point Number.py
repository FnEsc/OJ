import re
pattern=re.compile(r"^[+-]?[0-9]*\.[0-9]+$")
for _ in range(int(input())):
    print(bool(re.match(pattern,input())))