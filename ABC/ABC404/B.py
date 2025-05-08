N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

min_count = float('inf')

def count_diff(grid_1,grid_2,N):
    result  = 0
    for i in range(N):
        for j in range(N):
            if grid_1[i][j] != grid_2[i][j]:
                result += 1
    return result

def rotate90(grid,N):
    # N x N グリッドを90度右回転
    return [''.join([grid[N - j - 1][i] for j in range(N)]) for i in range(N)]

current = S

for i in range(4):
    diff = count_diff(current, T,N)
    min_count = min(min_count, diff + i)
    current = rotate90(current,N)

print(min_count)