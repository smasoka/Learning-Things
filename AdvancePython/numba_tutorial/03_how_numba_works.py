from numba import jit

@jit
def add(a, b):
    return a + b

# Notice the types
print(add(1,1))
print(add.inspect_types())

# Notice what its doing here .....
print(add(1., 1.))
print(add.inspect_types())

# We can do this - see if you understand
# for k, v in add.inspect_llvm().items():
#     print(k, v)

# Lets check strings
@jit
def add_strings(a, b):
    return a + b

print(add_strings('a', 'b'))
print(add_strings.inspect_types())

# nopython mode - run without the Python Interpreter - Best performance
@jit(nopython=True)
def add_strings(a, b):
    return a + b

print(add_strings('a', 'b'))
print(add_strings.inspect_types())

# A shortcut for 'nopython=True'
from numba import njit

@njit
def add_more_strings(c, d):
    return c + d

print(add_more_strings('c', 'd'))
print(add_more_strings.inspect_types())

# more flags you can pass

# cache=True
# nogil=True