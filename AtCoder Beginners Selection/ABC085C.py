N, Y = map(int,input().split())
result_x = result_y = result_z = -1
for x in range(N+1):
    for y in range(N-x+1):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            result_x = x
            result_y = y
            result_z = z
            break
print(result_x, result_y, result_z)