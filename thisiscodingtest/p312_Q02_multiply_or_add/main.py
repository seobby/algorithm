
lst = [int(i) for i in input()]

result = lst[0]
for i in range(1, len(lst)):
    if result <= 1 or lst[i] <= 1:
        result += lst[i]
    else:
        result *= lst[i]

print(result)

