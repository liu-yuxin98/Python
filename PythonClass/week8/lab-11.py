






'''
lst = [1,2,3,[4,5,6],7,8,[9,10,11,[12,13]],14]
numlst = []  # 用于记录这一层的int数字
nextlst = []  # 用于记录下一层处理后的lst，作为变量
for num in lst:
    if type(num) == int:
        numlst.append(num)
    else:
        nextlst.extend(num)
print(numlst)
print(nextlst)

'''






















# code-1
# 函数

'''
def w( a, b, c):
   if a == 1:
    return 1
   elif a ==2 :
       return 2



# input
inputlst = []
while True:
    numlst = [int(i) for i in input().split()]
    if numlst == [-1, -1, -1]:
        break
    inputlst.append(numlst)

for i in range(len(inputlst)):
    a, b, c = inputlst[i][0], inputlst[i][1], inputlst[i][2]
    ans = w(a, b, c)
    print('w({}, {}, {})'.format(a, b, c), end=' ')
    print('= ' + str(ans))


'''




'''
# code-3
n = int(input().strip())
num = input().split()
numlst = [int(i) for i in num]
numlst.sort()
gift = 0
i = 0
while True:
    if i > len(numlst)- 3:
        break
    if numlst[i+2] - numlst[i+1] == 1 and numlst[i+1] - numlst[i] == 1:
        gift += 1
        i = i + 3
    else:
        i += 1
print(gift)


'''



'''
# code-2

def rabbit(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 1]
    else:
        oldlst = rabbit(n-1)
        newlst = oldlst[::]
        newr = sum(oldlst[:n-2])
        newlst.append(newr)
        return newlst
n = int(input().strip())
print(sum(rabbit(n)))
'''






'''
def Fun_fact(n) :
    if n < 2:
        return 1
    else:
        return n*Fun_fact(n-1)

def Fact_output(m):
    x = []
    y = 0
    i = 1
    while True:
        if i > 2*m-1:
            break
        x.append( str(i)+'!' )
        y += Fun_fact(i)
        i += 2
    x = '+'.join(x)
    return x, y

factx = int( input())
resultx,resulty = Fact_output(factx)
s_format = "{} = {}".format(resultx,resulty)
print(s_format)
'''



