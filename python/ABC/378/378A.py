from collections import Counter

A = list(map(int,input().split()))

count = Counter(A)
result = sum(value // 2 for value in count.values())


print(result)