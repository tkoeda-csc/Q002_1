N = int(input())
S = input().split()

dup = set()
final = []


def duplicate(n, s):
    for i in range(n):
        if s[i] in dup:
            return "NO"
        dup.add(s[i])
    return "YES"


print(duplicate(N, S))
