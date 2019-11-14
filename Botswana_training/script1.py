#!/anaconda3/bin/python

print("Hello World!")

my_list = [3,6, 10, 56, -1, 4, 200, 135]
print(my_list)
print(my_list[5])

print(my_list[7])
print("Negetive indexing:{}".format(my_list[-1]))

print(my_list[4:8] )
print(my_list[2:4])
print(my_list[1:-1])
print(my_list[1:])
print(my_list[:-2])

my_names = ["Sakhile", "Krishna", "Daniel"]
print(my_names)
my_names.insert(1, "Thato")
print(my_names)
my_names.append("Ayanda")
print(my_names)
my_names.remove("Krishna")
print(my_names)
print(my_names.pop())
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)

my_names = ["Sakhile", "Krishna", "Daniel"]
print("Krishna" in my_names)
print(5 in my_list)
# use the if-else statement
if 135 in my_list:
    print("{} exists in my list)".format(135))
else:
    print("{} doesn't exist in my list".format(135))










