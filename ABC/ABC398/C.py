from collections import Counter
N = int(input())
A = list(map(int,input().split()))

count = Counter(A)

only_one = [num for num, count in count.items() if count == 1]

sorted_only_one = sorted(only_one, reverse=True)

if len(sorted_only_one) == 0:
    print(-1)
else:
    print(A.index(sorted_only_one[0])+1)