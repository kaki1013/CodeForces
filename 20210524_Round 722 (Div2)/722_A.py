# 틀림
#t = int(input())
#for _ in range(t):
#    n = int(input())
#    a = input().split()
#    print(n - a.count(min(a)))

# accepted
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i == min(a):
            count += 1
    print(n - count)