from sys import stdin
input = stdin.readline

t = int(input())  # 97~122
for _ in range(t):
    string = input().rstrip()
    n = len(string)
    isAlpha = True
    idx = -1
    for i in range(n):
        if string[i] == 'a':
            idx = i
    if idx == -1:
        isAlpha = False
    else:  # have 'a'
        curr = 97
        if idx == 0:
            for i in range(n):
                if ord(string[idx+i]) != 97 + i:
                    isAlpha = False
                    break
        elif idx == n - 1:
            for i in range(n):
                if ord(string[idx-i]) != 97 + i:
                    isAlpha = False
                    break
        else:  # 0 < idx < n - 1
            left, right = idx - 1, idx + 1
            while True:
                if not isAlpha or left < 0 or right > n - 1:
                    break
                A, B = ord(string[left]) == curr + 1, ord(string[right]) == curr + 1
                if (not A and B) or (A and not B):  # only one is True
                    if A:
                        left -= 1
                        curr += 1
                    if B:
                        right += 1
                        curr += 1
                else:
                    isAlpha = False
                    break
            if isAlpha and left == -1:
                for i in range(right, n):
                    if ord(string[i]) != curr + 1 + i - right:
                        isAlpha = False
                        break
            elif isAlpha and right == n:
                for i in range(left+1):
                    if ord(string[left - i]) != curr + 1 + i:
                        isAlpha = False
                        break
    if isAlpha:
        print('Yes')
    else:
        print('No')
