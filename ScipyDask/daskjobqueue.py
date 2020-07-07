from dask_jobqueue import PBSCluster 

cluster = PBSCluster()
cluster.scale(10)

from dask.distributed import Client
client = Client(clsuter)

# Do compute
# This is the simplest setup 

# -----------------------------------------------------------------------------------------------------------------------
# A  bit more

pcluster = PBSCluster(cores=36, memory='100GB', project='SOMETHING', queue='smp', interface='ib0', walltime='03:00:00')
pcluster.scale(100)

client = Client(pcluster)

# -----------------------------------------------------------------------------------------------------------------------
# 