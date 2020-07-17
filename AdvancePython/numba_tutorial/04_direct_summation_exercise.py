import numpy as np 
from numba import jit, njit
from line_profiler import LineProfiler 

# Create custom dtypes
particle_dtype = np.dtype({'names':['x','y','z','m','phi'], 
                             'formats':[np.double, 
                                        np.double, 
                                        np.double, 
                                        np.double, 
                                        np.double]})

@njit
def create_n_random_particles(n, m, domain=1):
    '''
    Creates `n` particles with mass `m` with random coordinates
    between 0 and `domain`
    '''
    parts = np.zeros((n), dtype=particle_dtype)
    #attribute access only in @jitted function
    for p in parts:
        p.x = np.random.random() * domain
        p.y = np.random.random() * domain
        p.z = np.random.random() * domain
        p.m = m
        p.phi = 0
    return parts


parts = create_n_random_particles(1000, .001, 1)
print(parts[:3])

@njit
def distance(part1, part2):
    '''calculate the distance between two particles'''
    return ((part1.x - part2.x)**2 + 
            (part1.y - part2.y)**2 + 
            (part1.z - part2.z)**2)**.5

distance(parts[0], parts[1])

@njit
def direct_sum(particles):
    for i, target in enumerate(particles):
        for j, source in enumerate(particles):
            if i != j:
                r = distance(target, source)
                target.phi += source.m / r
                
    return particles

direct_sum(parts)

lp = LineProfiler()
lp.add_function(create_n_random_particles)
lp.add_function(distance)
lp_wrapper = lp(direct_sum)
lp_wrapper(parts)
print(lp.print_stats())
