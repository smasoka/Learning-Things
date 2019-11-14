#!/anaconda3/bin/python

print("script 2")

my_list = [45, 13, 20]
print(len(my_list))

for value in my_list:
    print(value**2)

x = [3, 6, 9, 10]
y = []
# y = x^2 +2x +1
# HINT: y = xi**2 +2*xi +1
for xi in x:
    s = xi**2 +2*xi +1
    y.append(s)
print(y)

# z = 2x^3 + x^4
z = []
for xi in x:
    s = 2*xi**3 + xi**4
    z.append(s)
print(z)

# range sequence
for i in range(10):
    if i % 2 == 0:
        print(i)

for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# If a number is divisible by 3, 
# instead of the number print "Fizz",
# if a number is divisible by 5,
# print "Buzz" and if the number
# is divisible by both 3 and 5,
# print "FizzBuzz".
# ----------------
# 1
# 2
# Fizz
# 4
