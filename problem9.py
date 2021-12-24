# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
for k in range(0, 500):
    for j in range(0, k):   
        for i in range(0, j):
            if (i + j + k == 1000) and (i**2 + j**2 == k**2) and (i < j < k):
                    print('Found!')
                    print(f'i={i} j={j} k={k} , i*j*k={i*j*k}')