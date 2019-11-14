#!/anaconda3/bin/python

names = ['Sakhile', 'Krishna', 'Daniel']
print(names)

if 'Fred' in names:
    print('Fred is found')
elif 'Martha' in names:
    print('Sakhile is found')
elif 'Krishna' in names:
    print('Krishna is found')
else:
    print('name not found')

mylist = [2,4,6,8,10,12,14,16,18,20]
num = 800
# 1. Check if a number ? exist on the list. Print (number) exist {else} print (number) doesn't exist
if num in mylist:
    print(num, 'Exists')
else:
    print('{} doesnt exist'.format(num))
#2. Print first 5 elements
print(mylist[:5])
#3. Print elements in position 2 - 8
print(mylist[2:8])
#4. Print the last 2 elements
print(mylist[-2:])
#5. Reverse the list
mylist.reverse()
#6. Print the list
print(mylist)







