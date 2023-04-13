N, M = map(int,input().split())
A = list(map(int,input().split()))

L = []
for i in range(N):
    L.append(i+1)

x = 1
result = []
for i in range(len(A)):
    if i < len(A)-1:
        if A[i] + 1 == A[i+1]:
            x += 1
            i += 1
            continue
    result.append([A[i]-(x-1), x])
    i += 1
    x = 1

ans = []
i = 0
if M == 0:
    i += N
    ans = L

for i in range(N):
    if L:
        if L[0] == result[0][0]:
            for j in range(result[0][1]+1):
                ans.append(result[0][1] + result[0][0] - j)
                L.pop(0)
            result.pop(0)
        else:
            aaa = L.pop(0)
            ans.append(aaa)
ans=[str(a) for a in ans]
ans=" ".join(ans)
print(ans)