from dask import get, delayed, visualize


def do_something_1(x, y):
    return x + y + 2*x*y

def do_something_2(a, b):
    return a**3 - b**3

def do_something_3(p, q):
    return p*p + q*q

def do_something_4(x):
    return x * 3

#  define the graph
dsk = {
    'thrice_1': (do_something_4, 10),
    'thrice_2': (do_something_4, 20),
    'thrice_3': (do_something_4, 30),
    'thrice_4': (do_something_4, 40),
    'square_sum': (do_something_3, 'thrice_1', 'thrice_2'),
    'a_plus_b_wholeSqaure': (do_something_1, 'square_sum', 'thrice_3'),
    'some_complex_stuff': (do_something_2, 'thrice_4', 'a_plus_b_wholeSqaure')
}

print(get(dsk, 'some_complex_stuff'))

visualize(dsk, rankdir="LR", filename="task_graph.png")

# Do More.....
