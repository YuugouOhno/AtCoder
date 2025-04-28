# N = int(input())
# S = input()

# seacret = []

# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             seacret.append(S[i]+S[j]+S[k])

# print(len(set(seacret)))

N = int(input())
S = list(input())

def safe_index(lst, value, start):
    return lst.index(value, start) if value in lst[start:] else -1

count = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            i_index = safe_index(S, str(i), 0)
            j_index = safe_index(S, str(j), i_index+1)
            k_index = safe_index(S, str(k), j_index+1)
            if i_index != -1 and j_index != -1 and k_index != -1:
                count += 1

print(count)