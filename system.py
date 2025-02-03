import os
import multiprocessing

# Using os module
num_cores_os = os.cpu_count()
print(f"Number of CPU cores (using os): {num_cores_os}")

# Using multiprocessing module
num_cores_mp = multiprocessing.cpu_count()
print(f"Number of CPU cores (using multiprocessing): {num_cores_mp}")