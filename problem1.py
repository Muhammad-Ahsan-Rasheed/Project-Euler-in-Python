n = int(input())
total = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        total += i
    else:
        continue
print(total)