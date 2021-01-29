from myOwnfunc import IsPrime
def FindPrimeFactor(number):
    num = []
    i = 2
    t = number
    count = 0
    if number<=1:
        print("please enter a number>=2")
        return None
    else:
        while i < number:
            if IsPrime.isPrime(i) and t % i == 0:
                while t % i == 0:
                    t = t / i
                    num.append(i)
            i += 1

    return num





