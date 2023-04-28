def find_longest_consecutive(nums):
    longest = 0  # 一番長い連続部分の長さを保持する変数
    current_length = 1  # 現在の連続部分の長さを保持する変数

    # リストを順番に走査し、連続部分の長さを更新する
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_length += 1
        else:
            longest = max(longest, current_length)
            current_length = 1

    # 最後の連続部分の長さを更新する
    longest = max(longest, current_length)

    return longest

def working_date(n,m):
    return [i for i in range(n, m+1)]

N = int(input())
all_date = []
for i in range(N):
    A, B = map(int,input().split())
    all_date = list(set(all_date) | set(working_date(A,B)))



print(find_longest_consecutive(sorted(all_date)))