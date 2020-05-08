# from collections import deque
# for _ in (range(int(input()))):
#     input()
#     side_lengths = deque(map(int, input().strip().split()))
#     result = "Yes"
#     while side_lengths:
#         m=max(side_lengths)
#         if m not in (side_lengths[0], side_lengths[-1]):
#             result = "No"
#             break
#         else:
#             side_lengths.remove(m)
#     print(result)

# 优化
for _ in (range(int(input()))):
    l=int(input())
    i=0
    side_lengths = list(map(int, input().split()))
    while i<l-1 and side_lengths[i]>=side_lengths[i+1]:
        i+=1
    while i<l-1 and side_lengths[i]<=side_lengths[i+1]:
        i+=1
    print("Yes" if i==l-1 else "No")