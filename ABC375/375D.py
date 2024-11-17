S = input()

S_l = len(S)

result = []
for i in range(S_l-2):
    indices = []
    index = S.find(S[i])
    while index != -1:
        indices.append(index)
        index = S.find(S[i], index + 1)
    if len(indices) >= 2:

        first_element = indices[0]
        differences = [x - first_element for x in indices[1:]]
        result+= differences
    S = S[-S_l+i:]
print(sum(result) - len(result))



