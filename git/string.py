def StringLen(String = "Hello World", String1 = "Hello friend"):
    if len(String) != len(String1):
        return False
    
    N = len(String)
    i = 0
    while i < N and String[i] == String1[i]:
        i = i + 1
    return i == N

print(StringLen())

