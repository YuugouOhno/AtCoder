from collections import Counter

N = str(input())

count = Counter(N)
if count["1"] == 1 and count["2"] == 2 and count["3"] == 3:
    print("Yes")
else:
    print("No")