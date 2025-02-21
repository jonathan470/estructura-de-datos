list = [5,1,8,9,12]
N = len(list)
i = 1

while i < N:
    Num_Actual = list[i]
    j = i - 1
    while j >= 0 and list[j] > Num_Actual:
        list[j + 1] = list[j]
        j = j - 1

    list[j + 1] = Num_Actual
    i = i + 1

print(list)

