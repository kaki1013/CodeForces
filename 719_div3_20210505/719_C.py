#    matrix = list([0]*n for _ in range(n))

#    matrix = list(list() for _ in range(n))
#    for l in matrix:
#        for _ in range(n):
#            l.append(0)
def which_matrix(n):
    matrix = list([0] * n for _ in range(n))
    for i in range((n ** 2 + 1) // 2):
        matrix[i // n][i % n] = 2 * i + 1
    for j in range(n ** 2 // 2):
        matrix[(j + (n ** 2 + 1) // 2) // n][(j + (n ** 2 + 1) // 2) % n] = 2 * (j + 1)
    return matrix


t = int(input())
for _ in range(t):
    n = int(input())
    if n ==1:
        print(1)
    elif n==2:
        print(-1)
    else:
        for line in which_matrix(n):
            for num in line:
                print(num, end=' ')
            print('')
