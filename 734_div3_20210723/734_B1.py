from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    string = input().rstrip()

    count = dict()
    for char in string:
        if char not in count:
            count[char] = 1
        else:
            if count[char] == 1:
                count[char] = 2
            if count[char] == 2:
                pass

    k, temp = 0, 0
    for key in count:
        if count[key] == 2:
            k += 1
        if count[key] == 1:
            if temp == 0:
                temp = 1
            elif temp == 1:
                temp = 0
                k += 1
    print(k)