import numpy as np
import cProfile
from line_profiler import LineProfiler 

def sum_array(inp):
    J, I = inp.shape

    # bad idea
    mysum = 0
    for j in range(J):
        for i in range(I):
            mysum += inp[j,i]
    
    return mysum

arr = np.random.random((300,300))

sum_array(arr)
cProfile.run('sum_array(arr)')
lp = LineProfiler()
lp_wrapper = lp(sum_array)
lp_wrapper(arr)
print(lp.print_stats())

############################## Now we use jit  ########################
from numba import jit

# jit function
sum_array_numba = jit()(sum_array)

sum_array_numba(arr)
cProfile.run('sum_array_numba(arr)')
lp = LineProfiler()
lp_wrapper = lp(sum_array_numba)
lp_wrapper(arr)
print(lp.print_stats())

######################### More common use as a Decorator #################
@jit
def sum_array(inp):
    J, I = inp.shape

    # bad idea
    mysum = 0
    for j in range(J):
        for i in range(I):
            mysum += inp[j,i]
    
    return mysum

sum_array(arr)
cProfile.run('sum_array(arr)')
lp = LineProfiler()
lp_wrapper = lp(sum_array)
lp_wrapper(arr)
print(lp.print_stats())




