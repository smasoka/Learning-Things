from time import time

profile_runs = {}


def add(*args, **kwargs):
    print("----", args, "-----")
    print(args[0][1])
    return sum(x for x in range(args[0][1]))

def product(x, y=2):
    return x * y


def speed_test(fn, *args, **kwargs):
    try:
        speed_test.calls += 1
        start_time = time()
        results = fn(*args, **kwargs)
        end_time = time()
        speed_test.run_time.append(end_time - start_time)

        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {speed_test.run_time[0]}")
        print(f"Call No: {speed_test.calls}")
        print(end_time - start_time)
        profile_runs[fn.__name__] = (speed_test.run_time, speed_test.calls)
        return results
    except Exception as e:
        print("Exception in {}".format(fn.__name__))
        print(e)
speed_test.calls = 0
speed_test.run_time = []

class TableProxy():
    
    profile_runs = {}
    
    def sum_nums_gen(*args, **kwargs):
        """Sum numbers from 0 to variable arg using gen"""
        something = speed_test(add, args, kwargs)
        return something
    
    def get_runs(self):
        return profile_runs

tr = TableProxy()
print(tr.sum_nums_gen(20))
print(tr.get_runs())