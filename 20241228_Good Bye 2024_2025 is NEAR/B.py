# # 실패
# def is_all_pinned(l, r, pinned):
#     for idx in range(l, r+1):
#         if idx not in pinned:
#             return False
#     return True
#
#
# for _ in range(int(input())):
#     n = int(input())
#     arr = [tuple(map(int, input().split())) for _ in range(n)]
#
#     pinned = [0]*(2*n)
#     for l, r in arr:
#         if l == r:
#             pinned[l-1] += 1
#     print(pinned)
#
#     ans = [0] * n
#     for l, r in arr:
#         if l == r:
#             if pinned[l-1] > 1:
#                 ans[l-1] = 0
#             else:  # 1
#                 pass
#
#         if is_all_pinned(l, r, pinned):
#             ans.append('0')
#         else:
#             ans.append('1')
#
#     print(ans)

def unique_impressions(t, test_cases):
    results = []

    for n, ranges in test_cases:
        max_val = max(r[1] for r in ranges)
        count = [0] * (max_val + 2)

        # Count overlapping ranges using sweep-line technique
        for l, r in ranges:
            count[l] += 1
            count[r + 1] -= 1

        # Prefix sum to get the number of ranges covering each value
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Determine uniqueness for each impression
        result = []
        for l, r in ranges:
            unique = False
            for v in range(l, r + 1):
                if count[v] == 1:  # Value is unique
                    unique = True
                    break
            result.append('1' if unique else '0')

        results.append("".join(result))

    return results

# Input reading
import sys
# input = sys.stdin.read
data = input().split()

t = int(data[0])
idx = 1

test_cases = []
for _ in range(t):
    n = int(data[idx])
    idx += 1
    ranges = []
    for __ in range(n):
        l, r = map(int, data[idx:idx + 2])
        ranges.append((l, r))
        idx += 2
    test_cases.append((n, ranges))

# Solve and output results
results = unique_impressions(t, test_cases)
sys.stdout.write("\n".join(results) + "\n")