
def reverse(number):
    rnumber=0
    if number<0:
        number=-1*number
        while number != 0:
            rnumber = 10 * rnumber + number % 10
            number = (number - number % 10) / 10
        rnumber=-1*rnumber
    else:
        while number != 0:
            rnumber = 10 * rnumber + number % 10
            number = (number - number % 10) / 10
        rnumber=rnumber

    return(rnumber)

