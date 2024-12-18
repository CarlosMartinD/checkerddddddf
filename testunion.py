import os
import time  # Import the time module to track time

# Configuration
num_files = 200
file_size = 2_000_000   # 200 KB approximately (200,000 bytes)
source_dir = "/unionfs"
target_dir = "/prueba"

# Create directories if they don't exist
os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

# Start tracking time
start_time = time.time()

print("Creating files...")
for i in range(num_files):
    file_name = f"file_{i+1:04d}.txt"
    file_path = os.path.join(source_dir, file_name)
    # Write arbitrary data; for binary data, we can just write null bytes or random data
    with open(file_path, "wb") as f:
        f.write(b'\x00' * file_size)  # Writing 200,000 null bytes

# End tracking time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Created {num_files} files of ~2MB each in '{source_dir}'.")
print(f"Time taken: {elapsed_time:.2f} seconds.")
