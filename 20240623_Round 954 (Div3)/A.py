def f(a, x, y, z):
    return abs(x-a)+abs(y-a)+abs(z-a)

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    tmp = [f(i, x, y, z) for i in range(1, 11)]
    print(min(tmp))
