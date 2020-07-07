import cProfile
import numpy as np 

from time import sleep
from line_profiler import LineProfiler 

def bad_call(dude):
    sleep(.5)

def worse_call(dude):
    sleep(1)

def sumulate(foo):
    if not isinstance(foo, int):
        return

    a = np.random.random((1000, 1000))
    a @ a

    ans = 0
    for i in range(foo):
        ans += i

    bad_call(ans)
    worse_call(ans)

    return ans

if __name__ == "__main__":
    print(sumulate(150))
    cProfile.run('sumulate(150)')
    lp = LineProfiler()
    lp.add_function(bad_call)
    lp.add_function(worse_call)
    lp_wrapper = lp(sumulate)
    lp_wrapper(150)
    print(lp.print_stats())
