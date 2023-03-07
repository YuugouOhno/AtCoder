N, Q = map(int,input().split())
player = [0]*N
l = []
for i in range(Q):
    event, x = map(int,input().split())
    if event == 1:
        player[x-1] += 1
    elif event == 2:
        player[x-1] += 2
    elif event == 3:
        if player[x-1] >= 2:
            l.append("Yes")
        else:
            l.append("No")
for i in l:
    print(i)