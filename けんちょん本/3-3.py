n = int(input()) 
a = list(map(int,input().split()))

min = 10000
second_min = 10000

for i in range(n):
    if a[i] <  min:
        second_min = min
        min = a[i]
    elif a[i] < second_min:
        second_min = a[i]

print(second_min)