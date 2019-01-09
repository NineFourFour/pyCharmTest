# 1
print('one' 'two')
# output
# onetwo

# 2
srt = 'Tech Beamers'
print(srt[::-1])
# output
# sremaeB hceT

# 3
# which of path, path1, path2, path3 will print out C:\Common\TestString.doc
path='C:\\Common\TestString.doc'
print(path)
path1='C:\Common\TestStri\ng.doc'
print(path1)
path2='C:\\Commo\n\TestSt\ring.doc'
print(path2)
path3='''C:\\Common\testString.doc'''
print(path3)
# output
# C:\Common\TestString.doc
# C:\Common\TestStri
# g.doc
# C:\Commo
# ing.doc
# C:\Common	estString.doc

#4
repl='Hello World'
print(repl.replace('l','n',2))
# replace(old, new, the number of times the new letter will replace the old letter in the string)
# The third argument
# In the current string there are three l,
# if the third argument is 1 then the first l will only be replaced by an n, eg. 'Henlo World'
# if 3 then the three l's will be replaced to give 'Henno Wornd'
#
# output
# Henno World

# 5
str1 = "bad"
str2 = "bad"
print(id(str1),id(str2))

# 6
print (R'Tech\nBeamers')
# output
# Tech\nBeamers

# 7
#
str='Recurssion'
print(str.rfind('s'))
# ans
# 6
# rFind method returns the highest index at which the string is found.

# 8
itemAss='Tech Beamers'
#itemAss[4]='-'
#TypeError: 'str' object does not support item assignment
itemAss = itemAss.replace(' ','-')
print ('item:',itemAss)

#9
class  Assign:
    def __init__(self, value= 0):
       self.__value =value

obj1 = Assign(2)
obj2 = Assign(2)
print(id(obj1) == id(obj2))
# output
# False
print(obj2._Assign__value)
# output
# 2

#10
capital='good-BYE' ' hello'
print(capital.capitalize())
# output
# Good-bye hello
# The first letter of the string is converted to uppercase and the others are converted to lowercase.

print(capital.upper())
# output
# GOOD-BYE HELLO


#11
cen='example'
print  (cen.center(2,'*'))
# output
# example
# Note: Padding will be done so that total length of string equals the width given. In this example it is ‘2’ since this is less than length of string so no padding is done.
print(cen.center(40,'@'))
# output
# @@@@@@@@@@@@@@@@example@@@@@@@@@@@@@@@@@
# length is 40, the string is at the center, '@' is the padding at the front and rear of the string

print((75+85+75)/3)



