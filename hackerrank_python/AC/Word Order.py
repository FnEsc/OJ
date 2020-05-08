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
