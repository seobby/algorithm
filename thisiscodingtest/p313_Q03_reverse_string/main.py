
lst = [int(i) for i in input()]

count0 = 0
count1 = 0

if lst[0] == 1:
    count0 += 1
else:
    count1 += 1

for i in range(len(lst)-1):
    if lst[i] != lst[i+1]:
        if lst[i+1] == 1:
            count0 += 1
        else:
            count1 += 1


print(min(count0, count1))

