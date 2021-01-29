# encoding=utf-8
class Count:
    def __init__(self,count=0,times=1):
        self.__count=count # 双下划线表示这是私有数据，不可访问
        self.times=times

c=Count()
#print(c.count) #不可访问
print(c.times)

'''
def main():
    c=Count() 
    n=1  
    print(c.count)
    print(n)
    f(c,n)
    print("after f")
    print(c.count)
    print(n)
    g(c,n)
    print("after g")
    print(c.count)
    print(n)

def f(c,n):
    c=Count(5)
    n=3
def g(c,n):
    c.count+=1
    n+=1
    return n
main()
'''
