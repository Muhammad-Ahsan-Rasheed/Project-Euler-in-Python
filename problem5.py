def smallest_multiple(n):
    i = n
    while True:
        if all(i % j == 0 for j in range(1, n + 1)):
            return i
        i += n
print(smallest_multiple(20))