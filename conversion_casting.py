# a=3
# print('%f' %a) # 3.000000
# print('%.2f' %a) # 3.00
# print(float(a)) # 3.0
# print('%s' %a) # 3
# print(str(a)) # 3

# b=4.7
# print(type(b))  # <class 'float'>
# print(float(b)) # 4.7
# print('%f' %b) # 4.700000
# print('%.1f' %b) # 4.7
# print(int(b)) # 4
# print('%d' %b)  # 4
# print('%i' %b) # 4
# print('%s' %b)   # 4.7

# c='python'
# print(int(c))
# print(float(c))

# d='5'
# print(int(d)) # 5
# print(float(d)) # 5.0
# print('%s' %d) # 5
# print('%d' %d) # TypeError:%d format: a real number is required , not str
# print('%f' %d) # TypeError: must be real number , not str


# e='6.7'
# print(int(e)) # ValueError: invalid literal
# print(float(e)) # 6.7
# f=float(e)
# print(int(f)) # 6

'''
Name:
Qualification:
Age:
Percentage:

My Name is xyz. Qualification is UG/PG 
Age: 20 and Percentage is 88.88%
'''

Name='HD'
Qualification='M.Tech'
Age=26
Percentage=88.88

print('My Name is',Name+'.'+'Qualification is',Qualification)
print('Age:',Age,'and Percentage is',str(Percentage)+'%')

print('My Name is'+' '+Name+'.'+'Qualification is'+' '+Qualification)
print('Age:'+' '+str(Age)+' '+'and Percentage is'+' '+str(Percentage)+'%')

print('My Name is %s. Qualification is %s' % (Name,Qualification))
print("Age: %d and Percentage is %.2f" %(Age,Percentage))