S = input()
n = len(S)

curr = 0
for ch in reversed(S):
    d = ord(ch) - ord('0')
    r = curr % 10

    if r <= d:
        curr += (d - r)
    else:
        curr += (10 - r) + d

print(n + curr)
