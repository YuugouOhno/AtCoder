N, K = map(int,input().split())
S = list(input())
member = 0
for i, result  in enumerate(S):
    if result == "o":
        if member >= K:
            S[i] = "x"
        member += 1
print("".join(S))