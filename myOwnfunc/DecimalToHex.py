def DecimalToHex(dec):
    hex=''
    while dec!=0:
        hexValue=dec%16
        hex=toHexChar(hexValue)+hex
        dec=dec//16
    return hex

def toHexChar(hexValue):
    if 0<=hexValue<=9:
        return chr(hexValue+ord('0'))
    else:
        return chr(hexValue-10+ord('a'))





num=1234
print('%#x' %num)
print(DecimalToHex(num))