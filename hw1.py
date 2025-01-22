import os
import shutil
import sys
import fakedir

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {path}: {e}")

def copy_and_sort_files(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                copy_and_sort_files(source_path, destination_dir)
            elif os.path.isfile(source_path):
                file_extension = os.path.splitext(item)[1][1:].lower() or "no_extension"
                target_dir = os.path.join(destination_dir, file_extension)
                create_directory(target_dir)
                try:
                    shutil.copy2(source_path, target_dir)
                    print(f"Copied file {source_path} to {target_dir}")
                except Exception as e:
                    print(f"Failed to copy file {source_path}: {e}")
    except Exception as e:
        print(f"Error processing directory {source_dir}: {e}")

def main():
    fakedir.create()

    source_dir = os.path.expanduser("/Users/siangicher/Documents/Projects/homework/goit-algo-hw-03/goit-algo-hw-03/test_folders")
    destination_dir = os.path.expanduser("/Users/siangicher/Documents/Projects/homework/goit-algo-hw-03/goit-algo-hw-03/destination")

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        sys.exit(1)

    copy_and_sort_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()