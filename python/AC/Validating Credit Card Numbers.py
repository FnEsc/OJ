import re
pattern=re.compile(r"^(?!.*(\d)(-?\1){3})([456]\d{3})(-?\d{4}){3}$")
# pattern也可以分开 r"^" r"(?!.*(\d)(-?\1){3})" r"([456]\d{3})(-?\d{4}){3}$"
for _ in range(int(input())):
    m=re.match(pattern,input())
    print("Valid" if m else "Invalid")