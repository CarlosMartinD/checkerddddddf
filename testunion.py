import os

# Configuration
num_files = 200
file_size = 200_000   # 200 KB approximately (200,000 bytes)
source_dir = "/unionfs-test"
target_dir = "/prueba"

# Create directories if they don't exist
os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

print("Creating files...")
for i in range(num_files):
    file_name = f"file_{i+1:04d}.txt"
    file_path = os.path.join(source_dir, file_name)
    # Write arbitrary data; for binary data, we can just write null bytes or random data
    with open(file_path, "wb") as f:
        f.write(b'\x00' * file_size)  # Writing 200,000 null bytes

print(f"Created {num_files} files of ~200KB each in '{source_dir}'.")
