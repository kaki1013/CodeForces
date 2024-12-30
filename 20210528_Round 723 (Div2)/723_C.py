n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
sum = 0
count = 0

for n in arr:
    if sum + n >= 0:
        sum += n
        count += 1
    else:
        break
print(count)

# dp, 빼면서 확인