import itertools
n = input()
ans = 0
for i in range(1,len(n)+1):
    for j in itertools.product(['7', '5', '3'], repeat=i):
        created = ''.join(j)
        if int(created) <= int(n) and '7' in created and '5' in created and '3' in created:
            ans += 1
print(ans)