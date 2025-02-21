list = [5,1,8,9,12]
N = len(list)
i = 1

while i < N:
    current = list[i]
    j = i - 1
    while j >= 0 and list[j] > current:
        list[j + 1] = list[j]
        j = j - 1

    list[j + 1] = current
    i = i + 1

print(list)

