#!/anaconda3/bin/python

print("Script 3")

mylist = [10, 24, -34]
print(mylist)
mylist[1] = 25
print(mylist)
# loop through mylist
for my_val in mylist: 
    print(my_val) 
for my_val in mylist:
    print(my_val * 2)

# To get the index position of the loop
for idx, val in  enumerate(mylist):
    print(idx,"-->",val)

# Use enumerate with the index to update the mylist: Multiply every element by 3. e.g list[0] = 10 * 3
for idx, val in enumerate(mylist):
    mylist[idx] = val * 3
print(mylist)

# Looping through Dictionaries
dict3 = dict(u=3, v=5, w=10)
# prints keys by default
for val in dict3:
    print(val)
# print values
for val in dict3.values():
    print(val)
# print key-value pair
for mykey,myvalue in dict3.items():
    print('{} --> {}'.format(mykey, myvalue)) 

# Enumerate key-value pairs
for idx, items in enumerate(dict3.items()):
    print('index:{} contains: {}'.format(idx,items))

mykey = "z"
for key in dict3.keys():
    if mykey == key:
        print(mykey, 'is found')
else:
    print(mykey, 'is not found')





dict4 = dict(list1=[1,2,3], list2=[2,4,6], list3=[3,6,9])
for lists in dict4.values():
    print(lists)
    for val in lists:    
        print(val)


# Range in a Loop
for val in range(0,10,2):
    print(val)
for val in range(10):
    print(val)


mykey = "v"
for key in dict3.keys():
    if mykey == key:
        print(mykey, 'is found')
        break
#    else:
#        print(mykey, 'is not found')
else:
    print(mykey, 'is not found')














