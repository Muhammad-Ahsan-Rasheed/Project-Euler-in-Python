def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

largest = 0
for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        if is_palindrome(i) and is_palindrome(j):
            continue
        elif i * j == int(str(i * j)[::-1]):
            if i * j > largest:
                print(i,j)
                largest = i * j
            break
print(largest)