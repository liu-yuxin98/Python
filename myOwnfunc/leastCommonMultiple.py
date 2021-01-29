def lcm(x,y):# 最小公倍数，是对两个自然数说的
    if(x==0 or y==0):
        return 0
    elif(x>0 and y>0):
        max=x*y
        i=x
        while i<max :
            if(i%x==0 and i%y==0):
                return i
            else:
                i+=1
        return i
    '''
    elif(x>0 and y<0):
        y=-y
        max=x*y
        i = x
        while i < max:
            if (i % x == 0 and i % y == 0):
                return -i
            else:
                i += 1
        return -i
    elif(x<0 and y<0):
print(lcm(0,1))
print(lcm(6,4))
print(lcm(4,6))    
    '''







