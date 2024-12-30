for _ in range(int(input())):
    n, m, k = map(int, input().split())
    """
    m < k
    g(i) := the sum of all the numbers in the permutation on a prefix of length i that are not greater than m (<= m)
    f(i) := the sum of all the numbers in the permutation on a prefix of length i that are not less than k (>= k)
    
    maximize sum(i=1~n){f(i)} - sum(i=1~n){g(i)}
    -> maximize sum(i=1~n){f(i)} & minimize sum(i=1~n){g(i)}
    -> big number desc order + ... + small number asc order
    """
    # [n, ..., k] + [m+1, ..., k-1] + [1, ..., m]
    ans = [i for i in range(n, k-1, -1)] + [i for i in range(m+1, k)] + [i for i in range(1, m+1)]
    print(*ans)

