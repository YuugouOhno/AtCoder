n = int(input())

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1 ):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

result = 0

for i in range (1,n+1,2):
    if count_divisors(i) == 8:
        result += 1

print(result)
