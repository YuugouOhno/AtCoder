N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]
ans = [0] * N
i = 0
for b in B:
    preB = b
    while preB > 0:
        if preB <= A[i % N]:
            ans[i % N] += preB
            preB = 0
            i += 1
        elif preB > A[i % N]:
            preB -= A[i % N]
            ans[i % N] += A[i % N]
            i += 1
for i in ans:
    print(i)