# H, W, N = map(int, input().split())

# garbage_list = []

# def trush(type, n):
#     trush_count = 0
#     # コピーでループすれば、元のリストを安全に変更できる
#     for x, y in garbage_list[:]:
#         if (type == 1 and x == n) or (type == 2 and y == n):
#             garbage_list.remove((x, y))
#             trush_count += 1
#     return trush_count

# for _ in range(N):
#     X, Y = map(int, input().split())
#     garbage_list.append((X, Y))

# Q = int(input())

# for i in range(Q):
#     type, n = map(int, input().split())
#     print(trush(type, n))

H, W, N = map(int, input().split())
# 各行・各列ごとのゴミ位置リストを作成
row_map = [[] for _ in range(H + 1)]
col_map = [[] for _ in range(W + 1)]

for _ in range(N):
    x, y = map(int, input().split())
    row_map[x].append(y)  # 行 x に落ちているゴミの列番号 y を追加
    col_map[y].append(x)  # 列 y に落ちているゴミの行番号 x を追加

# 行／列が既に削除済みかどうかのフラグ
row_deleted = [False] * (H + 1)
col_deleted = [False] * (W + 1)

Q = int(input())
for _ in range(Q):
    t, n = map(int, input().split())
    # タイプ1：行 n のゴミ
    if t == 1:
        # 既に処理済みなら 0
        if row_deleted[n]:
            print(0)
            continue
        cnt = 0
        # その行に落ちていた各ゴミについて、
        # まだ列が有効かチェックしてカウント
        for y in row_map[n]:
            if not col_deleted[y]:
                cnt += 1
        row_deleted[n] = True  # 行 n を削除済みに
        print(cnt)

    # タイプ2：列 n のゴミ
    else:
        if col_deleted[n]:
            print(0)
            continue
        cnt = 0
        for x in col_map[n]:
            if not row_deleted[x]:
                cnt += 1
        col_deleted[n] = True  # 列 n を削除済みに
        print(cnt)
