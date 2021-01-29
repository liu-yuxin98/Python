def f(x, a=[]):
    if(x>=a[0]):
        print("x>=a[0]")
        return 1
    else:
        return 0

a=[1,2,3]
x=4
f(4,a)