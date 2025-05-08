import sys
sys.setrecursionlimit(1 << 25)

N, M = map(int, input().split())

# 隣接リストを作成
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

# 条件1: 辺の数が頂点数と一致しているか
if M != N:
    print("No")
    exit()

# 条件2: 各頂点の次数が2であるか
for d in degree[1:]:  # 0番は使っていないので無視
    if d != 2:
        print("No")
        exit()

# 条件3: 連結であるか（DFSでチェック）
visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

dfs(1)

if all(visited[1:]):  # 全頂点が訪問済みなら連結
    print("Yes")
else:
    print("No")
