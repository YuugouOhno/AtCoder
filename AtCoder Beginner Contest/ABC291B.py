n = int(input())
x = list(map(int,input().split()))
x.sort()
del x[0:n]
del x[-n:]
print(float(sum(x))/float(len(x)))