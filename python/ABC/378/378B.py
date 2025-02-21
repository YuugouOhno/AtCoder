# 0:28:06
N = int(input())
q_list = []
r_list = []
for i in range(N):
    q, r = map(int, input().split())
    q_list.append(q)
    r_list.append(r)
Q = int(input())
t_list = []
d_list = []
for i in range(Q):
    t, d = map(int, input().split())
    t_list.append(t-1)
    d_list.append(d)


for j in range(Q):
    day = d_list[j]
    garbage = t_list[j]

    now_r = day % q_list[garbage]
    if now_r == r_list[garbage]:
        result = day
    elif now_r < r_list[garbage]:
        result = day + r_list[garbage] - now_r
    elif now_r > r_list[garbage]:
        result = day + q_list[garbage] + r_list[garbage] - now_r

    print(result)