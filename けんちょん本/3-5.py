n = int(input()) 
a = list(map(int,input().split()))

is_even = True
count = 0

while is_even:
    for i in a:
        if i%2 == 1:
            is_even = False
            break
    else:
        count += 1
    a = [n//2 for n in a]

print(count)