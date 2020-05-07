import math
AB,BC=[int(input()) for _ in range(2)]
AC=(AB**2+BC**2)**(1/2)
BM=AC/2
cosA=(BC**2)/(2*BM*BC)
print(str(round(math.degrees(math.acos(cosA))))+"°")
