def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    pri = [p for p in range(2, n+1) if prime[p] ]
    return pri

if __name__ == '__main__':
    print(sum(SieveOfEratosthenes(2000000)))
