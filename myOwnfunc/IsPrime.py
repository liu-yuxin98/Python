import math
def isprime(n):
    prime = []
    if n == 1:
        return 0
    for x in range(2, n):
        for k in prime:
            if x % k == 0: # x is not a prime
                break
        else: # x is a prime
            prime.append(x)  # 逐步构建素数列表
            if n % x == 0: # x is prime check weather n%x == 0
                return 0
    else:
        return 1

def FindPrime(n): # find all prime number in range(0,n)
    prime = list(range(2, n+1))
    for x in prime:
        for k in range(2*x, n+1, x):
            if k in prime:
                prime.remove(k)
    return prime

