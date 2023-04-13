n = int(input()) 
a = list(map(int,input().split()))

min_val = 10000
max_val = -1

for i in range(n):
    if a[i] <  min:
        min_val = a[i]
    if a[i] > max:
        max_val = a[i]

print(max_val-min_val)