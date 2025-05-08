S = input()

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

for i in alphabet:
    if i not in S:
        print(i)
        break