# すごい時間かかった、、

N = int(input())
S = input()

ones = S[:(N+1)//2 - 1]
slach = S[(N+1)//2 - 1]
tows = S[(N+1)//2:]

if N%2 == 1 and all(one == "1" for one in ones) and slach == "/" and all(tow == "2" for tow in tows):
    print("Yes")
else:
    print("No")