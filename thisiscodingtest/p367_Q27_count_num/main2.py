from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
lst = list(map(int, input().split()))

first = bisect_left(lst, x)
last = bisect_right(lst, x)

if first == last:
    print(-1)
else:
    print(last - first)

