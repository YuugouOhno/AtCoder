# def saiyasu(r,g, ans):
#     array = []
#     if r < g:
#         num = r - 1
#         for _ in range(g-r):
#             array.append(num)
#             num += 1
#     elif r > g:
#         num = g - 1
#         for _ in range(r-g):
#             array.append(num)
#             num += 1
#     if r != g:
#         for i in array:
#             ans += min_list[i]
#     return ans

# ans = 0
# n, m = map(int, input().split())
# min_list = [10000000000] * (m-1)
# for i in range(n):
#     a = list(map(int,input().split()))
#     a_differences = [a[i+1] - a[i] for i in range(len(a)-1)]
#     for j in range(m-1):
#         if a_differences[j] < min_list[j]:
#             min_list[j] = a_differences[j]
# x = int(input())
# R = 1
# print(min_list)
# for i in range(x):
#     musi, G = map(int,input().split())
#     ans = saiyasu(R, G, ans)
#     print(R,G,ans)
#     R = G

# print(ans)