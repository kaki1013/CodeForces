# 실패
is_prime = [True] * (10**5+1)
is_prime[0] = False
is_prime[1] = False
for i in range(10**5+1):
    if is_prime[i]:
        for mult in range(2*i, 10**5+1, i):
            is_prime[mult] = False

primes = []
for i in range(10**5+1):
    if is_prime[i]:
        primes.append(i)


def get_prime_exp(x):
    d = dict()
    for p in primes:
        if p > x:
            break
        if x % p == 0:
            count = 0
            tmp = x
            while tmp % p == 0:
                count += 1
                tmp //= p
            d[p] = count
    return list(d.items())


for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    x_list = get_prime_exp(x)
    a_list = [get_prime_exp(ai) for ai in a]
    print(x_list)
    print(a_list)

    # div = [1, x]
    # for i in range(2, int(x**0.5)+1):
    #     if x % i == 0:
    #         div.append(i)
    #         div.append(x // i)
    # div = sorted(list(set(div)))
    # print(list(d_x.items()))

