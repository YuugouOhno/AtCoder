import math

N, K = map(int, input().split())
A_list = list(map(int,input().split()))

def digit_count(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1

result = 1
for i in range(N):
    result *= A_list[i]
    if len(str(result)) > K:
        result = 1

print(result)