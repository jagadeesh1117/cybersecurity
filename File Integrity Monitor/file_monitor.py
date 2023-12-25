import hashlib
import os
import time

def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def monitor_directory(directory_path):
    """
    Monitor a directory for changes in file integrity.
    """
    file_hashes = {}
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = calculate_hash(file_path)
            file_hashes[file_path] = file_hash
    
    while True:
        for dirpath, _, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if file_path not in file_hashes:
                    print(f"File {file_path} has been created!")
                    file_hashes[file_path] = calculate_hash(file_path)
                else:
                    current_hash = calculate_hash(file_path)
                    if current_hash != file_hashes[file_path]:
                        print(f"File {file_path} has been modified.")
                        file_hashes[file_path] = current_hash
        
        # Check for deleted files
        for file_path in list(file_hashes.keys()):
            if not os.path.exists(file_path):
                print(f"File {file_path} has been deleted!")
                del file_hashes[file_path]
        
        time.sleep(5)  # Adjust the interval between checks as needed

# Example usage
directory_to_monitor = '/Users/jagadeeshchowdary/Desktop/desktop/desktop/monitor'
monitor_directory(directory_to_monitor)
