# 入力受け取り
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

n = H * W
vals = [A[i][j] for i in range(H) for j in range(W)]

neighbors = [[] for _ in range(n)]
for i in range(H):
    for j in range(W):
        u = i * W + j
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                v = ni * W + nj
                neighbors[u].append(v)

used = [False] * n
max_xor = 0

def dfs(cur_xor: int):
    global max_xor

    for v in range(n):
        if not used[v]:
            break
    else:
        max_xor = max(max_xor, cur_xor)
        return

    used[v] = True
    dfs(cur_xor ^ vals[v])
    used[v] = False

    for u in neighbors[v]:
        if not used[u]:
            used[v] = used[u] = True
            dfs(cur_xor)
            used[v] = used[u] = False

dfs(0)

print(max_xor)
