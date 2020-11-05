from mpi4py import MPI
import sys
import random
import time
import numpy as np

tick = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

random.seed(rank)



initial_work = int(sys.argv[1])
round_num = int(sys.argv[2])

print(rank, ":", initial_work, round_num)

others = list(range(size))
others.remove(rank)
counter = 0
requests = []
for _ in range(initial_work//size):
    another = random.choice(others)
    data = 0
    comm.send(data, (rank+1)%size)
    # requests.append(req)

# comm.Barrier()

while counter < round_num:
    data = comm.recv()
    if data == round_num:
        for another in others:
            comm.send(data, another)
        counter += 1
    else:
        comm.send(data+1, random.choice(others))
#
# while counter < initial_work:
#     data = comm.recv()
#     fh.write(str(data))
#     data += 1
#     if counter == total_work:
#         counter += 1
#         for another in others:
#             comm.send(data, another)
#     else:
#         another = random.choice(others)
#         comm.send(data, another)

print("time", time.time() - tick)
# MPI.Request.Waitall(requests)