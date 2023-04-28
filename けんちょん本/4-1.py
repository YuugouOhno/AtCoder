def tori(n):
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 0
    elif n == 2:
        memo[2] = 1
    
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = tori(n-1) + tori(n-2) + tori(n-3)
        return memo[n]

n = int(input())
memo = [-1] * n
tori(n-1)
print(memo)