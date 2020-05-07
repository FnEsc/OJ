import re
for _ in range(int(input())):
    m=re.findall(r"(?<!^)#(?:[a-fA-F0-9]{3}){1,2}",input())
    print("\n".join(m)) if m else None