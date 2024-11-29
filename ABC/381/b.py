# 00:08:56
from collections import Counter

s = input()

counter = Counter(s)
s_value_nums  =counter.values()

if len(s)%2 == 0 and all(s[i] == s[i+1] for i in range(0,len(s),2)) and all(s_value_num == 2 for s_value_num in s_value_nums):
    print("Yes")
else:
    print("No")