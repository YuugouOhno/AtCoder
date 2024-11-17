N = int(input())
XY = [(0,0)]

for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

XY.append((0,0))

def get_distance(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**(1/2)

result = 0
for i in range(N+1):
    tmp_result = get_distance(XY[i][0],XY[i][1],XY[i+1][0],XY[i+1][1])
    result += tmp_result

print(result)
