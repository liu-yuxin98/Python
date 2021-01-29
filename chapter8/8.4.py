s1="Welcome"
s2="welcome"
isequal=bool(s1==s2)
print(isequal)
print('---------------')
isequal=bool(s1.lower()==s2.lower())
print(isequal)
print('---------------')
isequal=bool(s1.startswith('AAA'))
print(isequal)
print('---------------')
print(s1.__add__(s2))



