# 0:05:20

from collections import Counter

N, D = map(int,input().split())
S = input()

counter = Counter
empty = counter(S)["."]

print(empty + D)