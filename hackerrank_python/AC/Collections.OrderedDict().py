import collections
ordered_dictionary = collections.OrderedDict()
N=int(input())
for i in range(N):
    item, quantity = input().rsplit(None, 1)
    if item not in ordered_dictionary:
        ordered_dictionary[item]=int(quantity)
    else:
        ordered_dictionary[item]+=int(quantity)
for i in ordered_dictionary.items():
    print(*map(str,i))