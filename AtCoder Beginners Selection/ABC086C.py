N = int(input())
route = [[0,0,0]]
for i in range(N):
    txy = list(map(int,input().split()))
    route.append(txy)
x = True
for i in range(N):
    t_d =  route[i+1][0] - route[i][0]
    x_d =  abs(route[i+1][1] - route[i][1])
    y_d =  abs(route[i+1][2] - route[i][2])
    surplus = t_d - x_d - y_d
    if surplus<0 or surplus%2 == 1:
        x = False
        break
print("Yes") if x else print("No")