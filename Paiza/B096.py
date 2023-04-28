H, W = map(int, input().split())
field = [[0] * W] * H
boms = []
for i in range(H):
    l = list(input())
    boms.append([i for i, x in enumerate(l) if x == '#'])
for i in range(H):
    for bom in boms[i]:
        field[i] = [1] * W
        for j in range(H):
            field[j][bom] = 1
print(sum(map(sum, field)))