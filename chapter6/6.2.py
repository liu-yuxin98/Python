def sumDigits(number):
    sum=0
    if number<0:
        number=-1*number
    else:
        number=number
    while number != 0:
        sum = sum + number % 10
        number = (number - number % 10) / 10
    return sum

print(sumDigits(-12345))
