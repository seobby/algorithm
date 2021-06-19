
N, x = map(int, input().split())
lst = list(map(int, input().split()))

def find_first(lst, target):
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            if (mid == 0) or (mid >= 1 and lst[mid-1] < target):
                return mid
            else:
                end = mid-1
        elif lst[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return None

def find_last(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            if (mid == end) or (mid < end and lst[mid + 1] > target):
                return mid
            else:
                start = mid + 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


first = find_first(lst, x)
last = find_last(lst, x)

if first or last:
    print(last - first + 1)
else:
    print(-1)
