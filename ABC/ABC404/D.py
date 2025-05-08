from itertools import product

N, M = map(int, input().split())
C = list(map(int, input().split()))

# 動物ごとの出現マップ（どの動物園にいるか）
animal_in_which_zoo = [set() for _ in range(M)]
for i in range(M):
    tmp = list(map(int, input().split()))
    K, A = tmp[0], tmp[1:]
    animal_in_which_zoo[i] = set(a-1 for a in A)  # 0-indexedに

ans = float('inf')

# 動物園ごとの訪問回数の全組み合わせ（各園0～2回）
for visit_plan in product([0, 1, 2], repeat=N):
    # 各動物を何回見られるかをカウント
    animal_seen = [0] * M
    for zoo in range(N):
        times = visit_plan[zoo]
        if times == 0:
            continue
        for i in range(M):
            if zoo in animal_in_which_zoo[i]:
                animal_seen[i] += times
    
    # 全部の動物を2回以上見れてるかチェック
    if all(seen >= 2 for seen in animal_seen):
        cost = sum(visit_plan[zoo] * C[zoo] for zoo in range(N))
        ans = min(ans, cost)

print(ans)
