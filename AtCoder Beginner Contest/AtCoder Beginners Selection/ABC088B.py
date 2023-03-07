N = int(input())
a_list = sorted(list(map(int,input().split())), reverse=True)

r = 0
for i in range(N):
    if i%2 == 0:
        r += a_list[i]
    else:
        r -= a_list[i]
print(r)