s = input()

first_B = s.index("B")
s = s.replace('B', 'O', 1)
second_B = s.index("B")

if (first_B + second_B) % 2 == 1:
    ans = "Yes"
else:
    ans = "No"

K = s.index("K")
first_R = s.index("R")
s = s.replace('R', 'O', 1)
second_R = s.index("R")

if first_R < K and K < second_R and ans == "Yes":
    ans = "Yes"
else:
    ans = "No"

print(ans)