# 0:09:57

N, D = map(int,input().split())
S = list(input())
S.reverse()

for i in range(D):
    S[S.index("@")] = "."

S.reverse()

print("".join(S))