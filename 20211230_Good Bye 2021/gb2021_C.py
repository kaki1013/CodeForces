def find_set(x):
    while x != parents[x]:
        x = parents[x]
    return x


def union(x, y):
    xroot = find_set(x)
    yroot = find_set(y)
    parents[xroot] = yroot


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))     # 등차 수열로 만드는 데 필요한 최소 연산의 수
    ans = 0     # n == 1 or 2 라면 ans = 0
    if n > 2:
        # n*(n-1)/2 개의 순서쌍 중에서 특정 공차 d를 이루는 순서쌍의 수와 해당 순서쌍의 인덱스 (i, j)를 저장
        diff, pair = dict(), dict()
        for i in range(n):
            for j in range(i + 1, n):
                d = (a[j] - a[i]) / (j - i)
                if d in diff:
                    diff[d] += 1
                    pair[d].append((i, j))
                else:
                    diff[d] = 1
                    pair[d] = [(i, j)]
        max_component = 0   # 해당 공차를 사용할 것이기 때문에, 이미 완성 되어 연산이 필요가 없는 요소의 개수
        ans = sorted([(-diff[d], pair[d]) for d in diff])   # 실제로는 sort를 안 해도 됨
        for aa in ans:
            __, pair = aa   # 실제로 필요한 것은 순서쌍
            # 특정 공차를 이루는 순서쌍들 중에서 이미 등차수열을 이루는, 연결요소를 구성하는 원소의 개수 -> 최대값 := max_component
            # DSU로 계산
            parents = [x for x in range(n)]
            for x, y in pair:
                union(x, y)
            count = [0 for _ in range(n)]
            for i in range(n):
                count[find_set(i)] += 1
            max_component = max(max_component, max(count))
        ans = n - max_component     # 연산이 필요한 요소의 수 := 전체 요소의 수 - 연산이 필요 없는 요소의 수
    print(ans)
