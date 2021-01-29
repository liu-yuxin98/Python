#-*- coding:utf-8-*-   # 允许出现中文
from myOwnfunc import IsPrime # 从myOwnfunc 中调用 IsPrime.py


print(IsPrime.IsPrime(3)) # 调用isprime.py中调用IsPrime()

x=4
y=5
z=6
print(id(x))
print(id(y))
print(id(z))
