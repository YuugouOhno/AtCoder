# N, K = map(int, input().split())
# S = str(input())

# segments = S.split("X")
# num_berry = [len(segment)//K for segment in segments]

# print(sum(num_berry))

N, K = map(int, input().split())
S = input()

segments = S.split("X")
num_berry = sum(len(segment)//K for segment in segments)

print(num_berry)