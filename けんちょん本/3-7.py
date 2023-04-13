import itertools

s = input()
l = list(range(1,len(s)))
ans=int(s)

def wa(s,plus_position):
    result = 0
    s_next = s
    for i in reversed(plus_position):
        result += int(s_next[i:])
        s_next = s[:i]
    result += int(s_next)
    return result

for i in range(1,len(s)):
    plus_position = list(itertools.combinations(l,i))
    for j in plus_position:
        plus_position_list = list(j)
        ans += wa(s,plus_position_list)

print(ans)