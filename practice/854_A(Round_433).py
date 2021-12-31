# https://codeforces.com/problemset/problem/854/A
def coprime(a, b):
    if a == b:
        return False
    elif min(a, b) == 2:
        if a % 2 == 0 and b % 2 == 0:
            return False
        return True
    else:
        for i in range(2, min(a, b)):
            if a % i == 0 and b % i == 0:
                return False
        return True


n = int(input())
a = n // 2
b = n - a
while not coprime(a, b):
    a -= 1
    b += 1
print(a, b)