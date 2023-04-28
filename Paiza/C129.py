def check_array_equality(array1, array2):
    # 配列の長さが異なる場合は異なる構成とみなす
    if len(array1) != len(array2):
        return False

    # 配列の要素をソートして比較する
    sorted_array1 = sorted(array1)
    sorted_array2 = sorted(array2)

    # ソートされた配列が一致しない場合は異なる構成とみなす
    if sorted_array1 != sorted_array2:
        return "No"

    return "Yes"

# 入力を受け取る
N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
B = [int(input()) for _ in range(M)]

print(check_array_equality(A,B))