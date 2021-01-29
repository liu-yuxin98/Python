# encoding=utf-8
s="Helloworld"
print(len(s))# 字符串长度
print(min(s))# 按照ASCII码排序，选出最小的
print(s[-1]) # print the last charcater  s[-1]=s[len(s)-1]
print(s[0:5])# 截取片段
a='a'
print(ord('a')) #chr转ASCII码
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(chr(97)) # ASCII转chr
print("----------------")
# 字符串加法
s1="hello"
s2="python"
print(s1+"to"+s2)
# 字符串乘法
print(3*s1)
print("----------------")
# in and not 的说法
s="hellowelcome"
print("come" in s)
print("----------------")

# 比较字符串 >;<;==;!=
s1="jack"
s2="jane"
print(s1==s2)
print(s1!=s2)
print(s1>s2)
print(s1<s2) # 因为字符串比较大小是一一比较字母的ASCII码，第三个字母c<n 所以 s1<s2
print("----------------")
print("互换s1,s2")
s1,s2=s2,s1 #互换
print(s1)
print(s2)
print("----------------")

#迭代
s="abcdefghijk"
for ch in s:
    print(ch)
print("----------------")
for i in range (0,len(s),2):
    print(s[i])
print("----------------")

# 测试字符串
s="hellowold1244"
print(s.isalnum()) # 是都含有数字
print(s.isalpha()) # 是否全是字母
print(s.isdigit()) #是否是纯数字
print("----------------")

s="hello world I love you"
print(s)
print(s.isspace()) #方法检测字符串是否只由空格组成
for i in range(0,len(s)):
    if s[i].isspace():
        print(i)

print("----------------")

#搜索字符串
s="love"
s2="HHIIelajsdk love andaj love jasdlk love"
print(s2.endswith(s))  #是否以s结尾
print(s2.startswith(s)) #是否以s开头
print(s2.count(s)) #有几个s
print(s2.find(s)) #找到s在字符串中第一个出现时候的下标
print(s2.rfind(s))
print("----------------")
#字符串转化
print(s2.replace("love","flower")) #将love替换成flower
print(s2.lower()) #所有字母小写
print(s2.capitalize())#首字母大写
print(s2.title()) #每个单词首字母大写
print("----------------")
#删除空格
s="   welcome to python   "
print(s.lstrip()) #左空格
print(s.rstrip()) #右空格
print(s.strip()) #两边空格
print("----------------")
#格式化字符串
s="hello"
print(s.rjust(11,"*"))
print(s.center(11,"^"))
print(s.ljust(11,"-"))



