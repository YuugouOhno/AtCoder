n = input()
s = list(input())
area = [(0,0)]
for i, move in enumerate(s):
    if move == "R":
        next = (area[i][0]+1, area[i][1])
        area.append(next)
    elif move == "L":
        next = (area[i][0]-1, area[i][1])
        area.append(next)
    elif move == "U":
        next = (area[i][0], area[i][1]+1)
        area.append(next)
    elif move == "D":
        next = (area[i][0], area[i][1]-1)
        area.append(next)
print("No") if len(area) == len(set(area)) else print("Yes")