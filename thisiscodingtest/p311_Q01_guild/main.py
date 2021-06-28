
N = int(input())

lst = list(map(int, input().split()))
lst.sort()

grp = 0
ans = 0
for i in lst:
    grp += 1
    if grp >= i:
        ans += 1
        grp = 0

print(ans)


