from dask import delayed, compute

def do_something_1(x, y):
    return x + y + 2*x*y

def do_something_2(a, b):
    return a**3 - b**3

def do_something_3(p, q):
    return p*p + q*q

x = [2, 4, 6, 8, 10]
y = [3, 6, 9, 12, 15]
z = [10, 20, 30, 40, 50]

final_result = []

# Eager and Serial
for i in range(0, len(x)):
    res_1 = do_something_1(x[i], y[i])
    res_2 = do_something_2(y[i], z[i])
    res_3 = do_something_3(res_1, res_2)
    final_result.append(res_3)

print(final_result)
print(sum(final_result))

# Delayed
final_result = []
for i in range(0, len(x)):
    # Wrap the function calls inside delayed
    res_1 = delayed(do_something_1)(x[i], y[i])
    res_2 = delayed(do_something_2)(y[i], z[i])
    res_3 = delayed(do_something_3)(res_1, res_2)
    final_result.append(res_3)

final_sum = delayed(sum)(final_result)

print(final_sum)
print(final_sum.compute())
print(final_sum.visualize())

# Use decorators as well
@delayed
def do_something_1(x, y):
    return x + y + 2*x*y

@delayed
def do_something_2(a, b):
    return a**3 - b**3

@delayed
def do_something_3(p, q):
    return p*p + q*q

final_result = []
for i in range(0, len(x)):
    # Wrap the function calls inside delayed
    res_1 = do_something_1(x[i], y[i])
    res_2 = do_something_2(y[i], z[i])
    res_3 = do_something_3(res_1, res_2)
    final_result.append(res_3)

final_sum = delayed(sum)(final_result)

print(final_sum)
print(final_sum.compute())
print(final_sum.visualize())
