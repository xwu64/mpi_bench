from mpi4py import MPI
from time import sleep, time


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

sleep(rank)
comm.Barrier()
print(time())