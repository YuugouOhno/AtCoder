N = int(input())

A_list = []
B_list = []

for i in range(N):
    A,B=map(int,input().split())
    A_list.append(A)
    B_list.append(B)

A_list.sort()
B_list.sort()

# enter = sum(A_list)//N
# exit = sum(B_list)//N
enter = A_list[N // 2]
exit = B_list[N // 2]

result = 0
for i in range(N):
    result += abs(enter - A_list[i])+abs(exit - B_list[i])+abs(A_list[i] - B_list[i])

print(result)