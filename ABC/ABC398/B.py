from collections import Counter

A = list(map(int, input().split()))



def is_fullhouse(A):
    count = Counter(A)
    most_common = count.most_common(2)

    if len(most_common) <= 1:
        return False
    elif most_common[0][1] >= 3 and most_common[1][1] >= 2:
        return True
    else:
        return False


if is_fullhouse(A):
    print("Yes")
else:
    print("No")