N = int(input())
A = [list(input()) for _ in range(N)]

B = [row[:] for row in A]

for i in range(1,int(N/2)+1):
    for y in range(i,N+1-i+1):
        for x in range(i,N+1-i+1):
            B[y-1][N+1-x-1] = A[x-1][y-1]
    
    A = [row[:] for row in B]

for i in range(N):
    print("".join(A[i]))