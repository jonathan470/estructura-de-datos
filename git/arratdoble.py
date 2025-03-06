def arraydouble(array = [1, 7, 2, 21, 14]):
    Integer = len(array)
    New_array = [array] * (Integer * 2)

    j = 0

    while j < Integer:
        New_array[j] = array[j]
        j = j + 1

    return New_array

print(arraydouble())

