import os
import time  # Import the time module to track time

# Configuration
num_files = 200
file_size = 2_000_000   # 200 KB approximately (200,000 bytes)
source_dir = "/prueba"
target_dir = "/prueba"

# Create directories if they don't exist
os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

# Start tracking time for file creation
start_time_create = time.time()

print("Creating files...")
for i in range(num_files):
    file_name = f"file_{i+1:04d}.txt"
    file_path = os.path.join(source_dir, file_name)
    # Write arbitrary data; for binary data, we can just write null bytes or random data
    with open(file_path, "wb") as f:
        f.write(b'\x00' * file_size)  # Writing 200,000 null bytes

# End tracking time for file creation
end_time_create = time.time()

# Calculate the elapsed time for file creation
elapsed_time_create = end_time_create - start_time_create

print(f"Created {num_files} files of ~2MB each in '{source_dir}'.")
print(f"Time taken for creation: {elapsed_time_create:.2f} seconds.")

# Start tracking time for file reading
start_time_read = time.time()

print("Reading files...")
for i in range(num_files):
    file_name = f"file_{i+1:04d}.txt"
    file_path = os.path.join(source_dir, file_name)
    # Reading the file (just to simulate the read operation)
    with open(file_path, "rb") as f:
        f.read()  # Read the entire file (simulating processing)

# End tracking time for file reading
end_time_read = time.time()

# Calculate the elapsed time for file reading
elapsed_time_read = end_time_read - start_time_read

print(f"Read {num_files} files of ~2MB each from '{source_dir}'.")
print(f"Time taken for reading: {elapsed_time_read:.2f} seconds.")
