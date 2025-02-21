#python for atcoder

# -*- coding: utf-8 -*-
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

#一個の数字のインプット
a = int(input())

#n文字のアルファベットをインプット
a = str(input)

#a1 a2 ...のインプット(数字)（改行なし）
a = list(map(int, input().split()))
a = [int(i) for i in input().split()] #出力[a1,a2,a3,,,an]

#a1,a2,...のインプット(intをstrに変えれば文字列も可能)（改行）
a = [int(input()) for _ in range(n)]
a = []
for i in range(n):
    a.append(int(input()))

#A1,A2,,,N1,N2,,,のインプット(数字)（二次配列で出力）
n = int(input())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])

#上が文字列のとき
c = []
for i in range(h):
    c.append(list(str(input())))

#2つ以上の数字のインプット
a,b,c = [int(i) for i in input().split()]
a,b,c = map(int,input().split()) #strにも変更可能
#個人的に下がおすすめ
#2つの数字のインプットの時は、左辺を２文字にするだけ！

#aに配列としてたくさんのスペース区切りの数字をインプット
a = [int(i) for i in input().split()]

#文字を１文字ずつ分割してインプット
s = list(str(input()))

#12 hoge 3.14のような入力
(lambda x: [int(x[0]), x[1], float(x[2])])(input().split())
#x[0] = 12(整数) x[1] = "hoge"(文字列) s[2] = 3.14(小数)

#数字（ex.1234）を1けた区切りの配列に
a = list(str(input()))
for i in range(len(a)):
    a[i] = int(a[i])

#sに2次配列としてたくさんの文字をインプット(s[n]は一文字区切りの文字)
s = []
for i in range(N):
    s.append(list(str(input())))
#abc
#bcd
#cde
#[[a,b,c],[b,c,d],[c,d,e]]
#にする



#最大の整数（初期化のときなど）
2147483647
import sys
inf = sys.maxsize

#再帰上限の変更
import sys
sys.setrecursionlimit(3*10**6)

#GCD（最大公約数）
import fractions
fractions.gcd(a,b)
#または
def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

# 約数列挙
def divisors(n):
    """
    約数列挙

    Parameters
    ----------
    n : int
        n以下の約数を列挙する

    Returns
    ---------
    divisors_list : int in list
        約数の入ったリスト
    """

    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    divisors_list = lower_divisors + upper_divisors[::-1]
    return divisors_list

#最小公倍数
def lcm(a, b):
    return (a * b) // gcd(a, b)

# 拡張ユークリッドの互除法
def extgcd(a, b):
    """
    拡張ユークリッドの互除法

    Parameters
    ----------
    a : int
    ax + by = gcd(a, b)
    b : int
    ax + by = gcd(a, b)

    Returns
    ----------
    なんか, x, y
    """
    if b:
        d, y, x = extgcd(b, a%b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0

# 素数判定
def is_prime(n):
    """
    素数判定

    Parameters
    -----------
    n : int
        nが素数かどうかを判定

    Return
    -----------
    res : bool
        素数かどうか
    """

    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# エラトステネスのふるい
def sieve(n):
    """
    n以下の素数の数を求める

    Parameters
    ----------
    n : int
        n以下の素数の数を求める
    
    Return
    ----------
    p : int
        n以下の素数の数
    """

    p = 0
    prime = []
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            p += 1
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return p

# 素因数分解
def prime_factor(n):
    """
    自然数nを素因数分解する

    Parameters
    ---------------
    n : int
        自然数n
    
    Returns
    ---------------
    res : list of int
        素因数分解の結果
        [0, 0, 3, 0, 0, 0, 0, 0] -> 2^3
    """

    res = [0 for _ in range(n+1)]

    if n == 1:
        res[1] += 1
        return res
    else:
        for i in range(2, int(math.sqrt(n))+1):
            while n % i == 0:
                res[i] += 1
                n //= i
        if n != 1:
            res[n] += 1
        return res

c*d/gcd(c,d) #[c,d]での公倍数
lcm(a, b) = a * b // gcd(a, b)

a.upper() #大文字変換
a.lower() #小文字変換

a // b #切り捨て除算

a % b #aをbで割った余り

#演算子
#http://www.tohoho-web.com/python/operators.html

#スペース区切り出力
print("{} {}".format(a+b+c, s))

#平方数か
def try_square_root_naive(n):
    m = float(n**.5)
    return True if m == m // 1 else None

#桁数
len(str(b))

#1文字分割
list(str(x))  #list関数は、文字列(str)のみ！！整数型(int)はダメ！

#文字列（配列）を結合
test = ["ab" , "c" , "de" ]
result = "".join(test) #""の中の文字を区切り文字にできる

#ソート
a.sort()
b = sorted(a)

#アスキコード
ord('A') #アスキコードを返す関数
chr(N)   #アスキコードに対応する文字を返す関数

#改行なし出力
print(s, end = "")

#切り上げ切り捨て
import math
math.ceil(x / y) == (x + y - 1) // y
math.floor(x / y) = x // y

#ナップザック
def knapsack(N,W,weight,value): #N:weightの配列の個数　W:重さの限界
    #初期化
    inf=float("inf")
    dp=[[-inf for i in range(W+1)] for j in range(N+1)]
    for i in range(W+1): dp[0][i]=0

    #DP
    for i in range(N):
        for w in range(W+1):
            if weight[i]<=w: #dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
                dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
            else: #入る可能性はない
                dp[i+1][w]=dp[i][w]
    return dp[N][W]


alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#コンビネーション
def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

N = 110  # N は必要分だけ用意する
mod = pow(10, 9) + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


#正確な10進数の小数
#ライブラリ decimal

# UnionFind
def init(n):
    global par, rank
    par = [i for i in range(n)]
    rank = [0 for _ in range(n)]

# 木の根を求める
def find(x):
    global par, rank
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])   # 縮約の操作
        return par[x]

# xとyの属する集合を併合
def unite(x, y):
    global par, rank
    x = find(x)
    y = find(y)
    if x == y:
        pass
    else:
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

# xとyが同じ集合に属するか否か
def same(x, y):
    return find(x) == find(y)
