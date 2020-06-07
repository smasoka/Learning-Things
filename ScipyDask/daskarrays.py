import numpy as np
import dask.array as da
import time

np_arr = np.random.randint(20, size=20)
print(np_arr)

dask_arr = da.random.randint(20, size=20, chunks=3)
print(dask_arr.compute())
print(dask_arr.chunks)

dask_arr_from_np = da.from_array(np_arr, chunks=5)
print(dask_arr_from_np.compute())
print(dask_arr_from_np.chunks)

dask_arr_from_np.sum().visualize(rankdir="LR")

(dask_arr_from_np + 1).visualize(rankdir="LR")

dask_arr_mean = da.mean(dask_arr_from_np)
dask_arr_mean.compute()
dask_arr_mean.visualize(rankdir="LR")

x = da.random.random(10, chunks=2)
y = da.random.random(10, chunks=2)
sum_x_y = da.add(x,y)
mean_x_y = da.mean(sum_x_y)

sum_x_y.compute()
sum_x_y.visualize()
mean_x_y.visualize()

da_arr_large = da.random.randint(10000, size=(50000, 50000), chunks=(5000, 1000))
da_sum_large = da_arr_large.sum()

print(da_arr_large.nbytes/1e+9)
# print(da_sum_large.compute())

# Going Deeper

my_arr = da.random.randint(10, size=20, chunks=3)
print(my_arr.compute())
my_hundred_arr = my_arr + 100
print(my_hundred_arr.compute())
print((my_arr * (-1)).compute())

print(my_arr.sum().compute())
my_ones_arr = da.ones((10,10), chunks=2, dtype=int)
print(my_ones_arr.compute())

my_custom_arr = da.random.randint(10, size=(4,4), chunks=(1,4))
print(my_custom_arr.compute())
print(my_custom_arr.mean(axis=0).compute())
print(my_custom_arr.mean(axis=1).compute())

# supports slicing
print(my_custom_arr[1:3, 2:4].compute())

# Supports broadcasting
my_small_arr = da.ones(4, chunks=2)
brd_example1 = da.add(my_custom_arr, my_small_arr)
print(brd_example1.compute())

ten_arr = da.full_like(my_small_arr, 10)
brd_example2 = da.add(my_custom_arr, ten_arr)
print(brd_example2.compute())

# supports reshaping
print(my_custom_arr.shape)
custom_arr_1d = my_custom_arr.reshape(16)
print(custom_arr_1d.compute())

# supprts stacking
stacked_arr = da.stack([brd_example1, brd_example2])
print(stacked_arr.compute())
another_stacked = da.stack([brd_example1, brd_example2], axis=1)
print(another_stacked.compute())

# supports concatination
concate_arr = da.concatenate([brd_example1, brd_example2])
print(concate_arr.compute())
another_concate = da.concatenate([brd_example1, brd_example2], axis=1)
print(another_concate.compute())

# compare performance
size_tuple = (50000, 50000)
# np_arr = np.random.randint(10, size=size_tuple)
# np_arr2 = np.random.randint(10, size=size_tuple)
# can't even store the random values

chunks_tuple = (5000, 5000)
da_arr = da.random.randint(10, size=size_tuple,
                           chunks=chunks_tuple)
da_arr2 = da.random.randint(10, size=size_tuple,
                            chunks=chunks_tuple)
now = time.time()
(((da_arr * 2).T)**2 + da_arr2 + 100).sum(axis=1).mean().compute()
end = time.time()
print(end - now)


# Universal Functions gufunc
size_tuple = (500,500)
chunks_tuple = (10, 500)
da_arr = da.random.randint(10, size=size_tuple,
                           chunks=chunks_tuple)
da_arr2 = da.random.randint(10, size=size_tuple,
                            chunks=chunks_tuple)
def random_func(x):
    return np.mean((((x*2).T)**2), axis=0)

gufoo = da.gufunc(random_func, signature="(i)->()", output_dtypes=float,
                                                    vectorize=True)
random_op_arr = gufoo(da_arr)
print(random_op_arr.compute())
print(random_op_arr.shape)

# _gufunc as a decorator
@da.as_gufunc(signature="(m,n),(n,j)->(m,j)", output_dtypes=int, allow_rechunk=True)
def random_func(x, y):
    return np.matmul(x, y)**2

da_arr3 = da.random.randint(10, size=(200, 100), chunks=(10, 100))
da_arr4 = da.random.randint(10, size=(100, 300), chunks=(5,5))

random_matmul = random_func(da_arr3, da_arr4)
print(random_matmul.compute())
print(random_matmul.shape)
