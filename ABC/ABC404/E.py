N = int(input())
C = list(map(int, input().split()))
A = list(map(int, input().split()))

beans = [0] * N
for i in range(1, N):
    beans[i] = A[i-1]

ans = 0

for i in range(N - 1, 0, -1):
    if beans[i] > 0:
        ans += 1  # 操作回数 +1
        cnt = beans[i]
        for j in range(i - C[i - 1], i):
            if j >= 0:
                beans[j] += cnt
        beans[i] = 0  # 使い終わったので0に

print(ans)