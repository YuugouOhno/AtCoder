# 0:31:42

# N = int(input())
# S = input()

# indices = [i for i, char in enumerate(S) if char == "/"]

# November_list = []
# for index in indices:
#     ones = S[:index][::-1]
#     tows = S[index+1:]

#     if ones and ones[0] == "1":
#         fin_one_index = ones.index("2")
#         one_len = 1
#         if fin_one_index == -1:
#             one_len = len(ones)
#         else:
#             one_len = fin_one_index
#     else:
#         one_len = 0

#     if tows and tows[0] == "2":
#         fin_tow_index = tows.index("1")
#         tow_len = 1
#         if fin_tow_index == -1:
#             tow_len = len(ones)
#         else:
#             tow_len = fin_tow_index
#     else:
#         tow_len = 0

#     November_list.append(min(one_len,tow_len)*2+1)

# print(max(November_list))

N = int(input())
S = input()

# 左から右へ、各位置までに連続する `1` の長さを計算
left_ones = [0] * N
for i in range(N):
    if S[i] == '1':
        left_ones[i] = left_ones[i-1] + 1 if i > 0 else 1

# 右から左へ、各位置から連続する `2` の長さを計算
right_twos = [0] * N
for i in range(N-1, -1, -1):
    if S[i] == '2':
        right_twos[i] = right_twos[i+1] + 1 if i < N-1 else 1

# 各スラッシュの位置を探索して最大長を計算
max_length = 0
for i in range(N):
    if S[i] == '/':
        # スラッシュ前の `1` の連続長
        ones_len = left_ones[i-1] if i > 0 else 0
        # スラッシュ後の `2` の連続長
        twos_len = right_twos[i+1] if i < N-1 else 0
        # 11/22 文字列の長さを計算
        max_length = max(max_length, 2 * min(ones_len, twos_len) + 1)

print(max_length)