N, K = map(int,input().split())
A = set(list(map(int,input().split())))

for i in range(K):
    if not i in A:
        print(i)
        exit()
print(K)