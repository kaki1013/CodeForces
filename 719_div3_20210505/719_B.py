#def count_ord(n):
#    count = 0
#    for i in range(1, n + 1):
#        if len(set(list(str(i)))) == 1:
#            count += 1
#    return count

def count_ord(n):
    count = 0
    for i in range(1, n + 1):
        num_str = str(i)
        keep = True
        for posi in range(len(num_str) - 1):
            if num_str[posi] != num_str[posi + 1]:
                keep = False
                break
        if keep:
            count += 1
    return count


N = int(input())
for _ in range(N):
    n = int(input())
    print(count_ord(n))
