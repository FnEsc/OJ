import re
pattern_and=re.compile(r"(?!(^#))(?<= )&(?= )")
pattern_or=re.compile(r"(?!(^#))(?<= )\|\|(?= )")
for _ in range(int(input())):
    print(re.sub(pattern_or, "or",re.sub(pattern_and, "and", input())))