# -*- coding: utf-8 -*-
# 2020-03-23
# author Liu,Yuxin


'''
        循环
————————————————————————
素数：prime,不包括1
合数：composite= fact1*fact2 合数是素数的乘积




# 分解质因数
import math
x = int(input())

for k in range(2, int(math.sqrt(x))+1):
    while True:
        if x % k == 0:
            print(str(k))
            x = x/k
        elif x % k !=0:
            break
    if x == 1:
        break


# 分解质因数 改进
# 当x = 1 时可以提前结束循环
import math
x = int(input())
lst = [ ]
for k in range(2, int(math.sqrt(x))+1):
    while True:
        if x % k == 0:
            print(str(k))
            lst.append(k)
            x = x/k
        elif x % k !=0:
            break
print(lst)

# prime number 1
import math

x = int(input())
for k  in range(2, x):
    if x%k==0:
        print(str(x)+' is not a prime')
        break  # 可以跳过else
else: # 循环正常结束（遍历结束）
    print(str(x)+ 'is a prime')

for x in range(2, 101):
    for k in range(2, int(x/2)+1):
        if x % k == 0:
            break  # 可以跳过else
    else:
        print(x, end=' ')


import math
cnt = 0
x = 3
s = 2
while True:
    for k in range(2, int(math.sqrt(x))+1):
        if x % k == 0:
            break  # 可以跳过else
    else:
        print(x, end=' ')
        cnt += 1
        if cnt >= 10:
            s += x
        if cnt % 5 == 0:
            print()
    x += 1
    if cnt == 50:
        break


# 提速 （1）去除偶数 （2）到平方根, 只需要判断[2,sqrt(x)]之间的所有素数  打表，！好快啊
# get prime<100
import math
lst =[2] # first prime=2
for x in range(3,101,2): # step  = 2
    for k in range(2, int( math.sqrt(x) )+1 ):
        if x % k == 0:
            break
    else:
        lst.append(x)

# get 50 primes
lst = [2]
x = 3
cnt = 1
while True:
    for k in range(2, int( math.sqrt(x) )+1 ):
        if x % k == 0:
            break
    else:
        lst.append(x)
        cnt += 1
    x += 2
    if cnt == 50:
        break
print(lst)


# speed up
import math
#1 忽略偶数
#2 检查factors 的范围：[2, int(math.sqrt(x))+1]
#3 factors 只需要检查 [2, x) 内的素数就可以
import math
n = int(input())
prime = []
for x in range(2, n):
    for k in prime:
        if x % k == 0: # x is not a prime
            break
    else: # x is a prime
        prime.append(x)  # 逐步构建素数列表
        if n % x == 0: # x is prime check weather n%x == 0
            print(str(n)+'is not prime')
            break
else:
    print(str(n)+' is a prime')
'''
# 4 sieve of Eratosthenes
#所有合数都可被分解质因数，因此任意素数的任意倍数都不是素数
'''
n = int(input())
prime = list(range(2,n))
for k in range(2*2,n,2): # delete 2的倍数
    prime.remove(k)
for k in range(3*2,n,3):  # delete 3 的倍数
    prime.remove(k)
for k in range(5*2,n,5):  # delete 5 的倍数
    prime.remove(k)


# 完整方法
n = int(input())
prime = list( range(2, n))
for x in prime: #
    for k in range(x*2, n , x): # x is prime number
        if k in prime:
            prime.remove(k)
print(prime)

# 牛顿法
n = int(input())
guess = n/2
while True:
    if abs(guess*guess-n)<1e-3:
        break
    guess = (guess+n/guess)/2
print(guess)

'''
# 二分法求根
# mid
'''
if f(left)*f(right)>0->no roots

if f(left)*f(right)<0 然后判断f(mid) 
# repeat
    if f(mid)*f(left)<0 : right = mid
    if f(mid) * f(right)<0: left =mid 
    if f(mid)-0 <e end
    
# code:
f = input()
left, right = map(float, input().split())
x = left
fl = eval(f)
x = right
fr = eval(f)
while fl * fr < 0:
    mid = (right+left)/2
    x = mid
    fm = eval(f)
    if abs(fm)<1e-3:
        print('root is ' + str(mid))
        break
    else:
        if fl*fm <0:
            right = mid
        elif fr * fm <0:
            left = mid
        x = left
        fl = eval(f)
        x = right
        fr = eval(f)
else:
    print('no roots')

'''
i=1
while i<=5:
    num=1
    for j in range(1,i+1):
        print(num,end="G")
        num+=2
    print()
    i+=1