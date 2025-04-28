from collections import Counter

N = int(input())
P_list = list(map(int, input().split()))

counter = Counter(P_list)

r = 1
r_list = []

# Pを同じ長さの配列を作り0で埋める
r_list = [0] * N
sorted_P = sorted(P_list, reverse=True)

while sorted_P:
    x = sorted_P[0]
    k = counter[x]
    for i, p in enumerate(P_list):
        if p == x:
            r_list[i] = r
            P_list[i] = -1
    r += k
    sorted_P = sorted_P[k:]
    counter = Counter(sorted_P)

for i in r_list:
    print(i)