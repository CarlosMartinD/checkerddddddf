import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Configuration
num_files = 200
file_size = 200_000   # Approximately 200 KB
source_dir = "/unionfs"
target_dir = "/unionfs"
num_workers = 8  # Adjust number of threads here

os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

def create_file(file_index):
    file_name = f"file_{file_index+1:04d}.txt"
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, "wb") as f:
        f.write(b'\x00' * file_size)
    return file_name

print("Creating files with multiple threads...")

start_time = time.time()

# Create files in parallel
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    created_files = list(executor.map(create_file, range(num_files)))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Created {len(created_files)} files of ~200KB each in '{source_dir}' in {elapsed_time:.2f} seconds.")

def read_file(file_name):
    file_path = os.path.join(target_dir, file_name)
    # If the file does not exist in the target directory, we skip it
    if not os.path.exists(file_path):
        return 0
    with open(file_path, "rb") as f:
        data = f.read()
        return len(data)

print("Reading files from target directory with multiple threads...")

# Read files in parallel
target_files = os.listdir(target_dir)
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    sizes = list(executor.map(read_file, target_files))

count_files = len([s for s in sizes if s > 0])
total_read = sum(sizes)

print(f"Read {count_files} files, total size read: {total_read} bytes.")
