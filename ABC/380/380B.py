# S = str(input())[1:]

# temp_count = 0
# result = ""

# for i in S:
#     if i == "|":
#         result += str(temp_count) + " "
#         temp_count = 0
#     else:
#         temp_count += 1

# print(result)
# 入力を受け取る
S = input().strip()

# "|" を基準に分割して、各区間の "-" の個数をリストに格納
segments = S.split('|')  # '|' で分割
print(segments)
dash_counts = [len(segment) for segment in segments if segment]  # 各区間の "-" をカウント

# リストを空白区切りの文字列に変換して出力
print(" ".join(map(str, dash_counts)))
