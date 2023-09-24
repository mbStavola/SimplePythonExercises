import os, sys

target_directory = sys.argv[1] if len(sys.argv) > 1 else "."

def print_directory(dir, indentation_level):
    indentation = "\t" * indentation_level
    files = os.listdir(dir)

    for file in files:
        full_path = os.path.join(dir, file) 

        is_dir = os.path.isdir(full_path)
        if is_dir:
            print(f"{indentation}{file}/")
            print_directory(full_path, indentation_level + 1)
        else:
            print(f"{indentation}{file}")

print(f"{target_directory}/")
print_directory(os.path.abspath(target_directory), 1)

