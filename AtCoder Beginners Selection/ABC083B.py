N, A, B = map(int, input().split())

def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return int(sum(array))

x = 0

for n in range(N+1):
    if A <= digitSum(n) and B >= digitSum(n):
        x += n
    
print(x)
