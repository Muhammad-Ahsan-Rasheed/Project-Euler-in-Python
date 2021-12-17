def fibonacci(n):
    a = [1, 2]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
        if a[i] > 4000000:
            return a[:-1]
    return a

arr = fibonacci(1000)
print(arr)
total = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        total += arr[i]
print(total)
