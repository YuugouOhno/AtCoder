A,B,C,X,Y = map(int,input().split())

cost = 999999999999
for i in range(0, max(X,Y)*2+1, 2):
    cost = min(cost ,C * i  + A * max(0,X - i // 2) + B * max(0,Y - i // 2))

print(cost)