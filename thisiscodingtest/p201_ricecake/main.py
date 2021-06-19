
N, M = map(int, input().split())
lst = list(map(int, input().split()))


# height 높이로 떡을 잘랐을 때, total 길이만큼을 손님이 가져갈 수 있는지 체크하는 함수
def check(height, total):
    return sum([(i-height) for i in lst if i > height]) >= total


start = 1
end = max(lst)
ans = 0

# binary search를 이용하여, 해당 조건을 만족하는 최대 높이를 찾아나감
while start <= end:
    mid = (start + end) // 2

    if check(mid, M):
        ans = max(ans, mid)
        start = mid+1
    else:
        end = mid-1

print(ans)



