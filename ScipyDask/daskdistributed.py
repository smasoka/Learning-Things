# from dask.distributed import Client

# client = Client(processes=False, threads_per_worker=2, n_workers=3, memory_limit='2GB')

# print(client) 
# print(client.scheduler)
# print(dir(client))
# print(client.status)
# print(client.shutdown)
from dask.distributed import Client, LocalCluster

cluster = LocalCluster()

client = CLient(cluster)

print(client.scheduler)
print(client.workers)

