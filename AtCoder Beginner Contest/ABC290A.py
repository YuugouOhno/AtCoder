N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
x = 0
for i in B:
    x += A[i-1]
print(x)