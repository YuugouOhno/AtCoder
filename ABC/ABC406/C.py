class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def add(self, i, v):
        # 1-indexed
        while i <= self.n:
            self.tree[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


N = int(input())
P = list(map(int, input().split()))
# 前処理：単調区間の左右端
inc_l = [0] * N
dec_l = [0] * N
inc_r = [0] * N
dec_r = [0] * N

# 左から
inc_l[0] = 0
dec_l[0] = 0
for i in range(1, N):
    if P[i-1] < P[i]:
        inc_l[i] = inc_l[i-1]
    else:
        inc_l[i] = i
    if P[i-1] > P[i]:
        dec_l[i] = dec_l[i-1]
    else:
        dec_l[i] = i

# 右から
inc_r[N-1] = N-1
dec_r[N-1] = N-1
for i in range(N-2, -1, -1):
    if P[i] < P[i+1]:
        inc_r[i] = inc_r[i+1]
    else:
        inc_r[i] = i
    if P[i] > P[i+1]:
        dec_r[i] = dec_r[i+1]
    else:
        dec_r[i] = i

# 峰 (peak) と 谷 (valley) の検出
is_peak = [False] * N
is_valley = [False] * N
for i in range(1, N-1):
    if P[i-1] < P[i] > P[i+1]:
        is_peak[i] = True
    elif P[i-1] > P[i] < P[i+1]:
        is_valley[i] = True

# 谷 j ごとに、「decleft = dec_l[j]」でバケット
buckets = [[] for _ in range(N)]
dec_part = [0] * N
for j in range(1, N-1):
    if is_valley[j]:
        # 谷の右側は inc_r[j] - j 通りの終了位置が選べる
        dec_part[j] = inc_r[j] - j
        buckets[dec_l[j]].append(j)

# Fenwick 木を準備
bit = Fenwick(N)
ans = 0

# i を左端基準で進めつつ、decleft == i の谷を BIT に登録
for i in range(N):
    # dec_l[j] == i の谷を追加
    for j in buckets[i]:
        if dec_part[j] > 0:
            bit.add(j+1, dec_part[j])

    # i がピークなら寄与を計算
    if is_peak[i]:
        # 左側は inc_l[i] .. i-1 のどこを l に選んでも良い
        left_choices = i - inc_l[i]
        # 右端に置ける谷 j の範囲は (i, dec_r[i]]
        if left_choices > 0 and dec_r[i] > i:
            total_right = bit.range_sum(i+2, dec_r[i]+1)
            ans += left_choices * total_right

print(ans)