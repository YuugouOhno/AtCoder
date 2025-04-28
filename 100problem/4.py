N, M = map(int, input().split())

A_list =[]
result = 0

for i in range(N):
    A = list(map(int,input().split()))
    A_list.append(A)

for i in range(0, M-1):
    for j in range(i+1, M):
        point = 0
        for k in range(N):
            point += max(A_list[k][i],A_list[k][j])
        result = max(result, point)

print(result)