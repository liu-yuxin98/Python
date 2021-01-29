
num1=eval(input("num1="))
num2=eval(input("num2="))
gcd=1
k=1
while gcd<=num1:
    if(num1%gcd==0)and(num2%gcd==0):
        k=gcd
    gcd+=1

print(k)