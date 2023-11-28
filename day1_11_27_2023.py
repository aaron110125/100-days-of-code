#https://leetcode.com/problems/integer-to-roman/description/

x = 99
if x //50:
    print('L')
y = (x//10)
z = (x%10)
if z > 4:
    z = z - 5
    print(y*'X' + 'V' + z*'I')
else:
    print(y*'X' + z*'I')


""" 
x = 99

y = (x//10)
z = (x%10)
if z > 4:
    z = z - 5
    print(y*'X' + 'V' + z*'I')
else:
    print(y*'X' + z*'I')
"""