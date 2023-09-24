import os, sys

pid = sys.argv[1] if len(sys.argv) > 1 else os.getpid()

base_dir = f"/proc/{pid}"

print("Available attributes:")
for file in os.listdir(base_dir):
    full_path = os.path.join(base_dir, file)

    is_dir = os.path.isdir(full_path)
    is_readable = os.access(full_path, os.R_OK)

    if is_dir or not is_readable:
        continue

    print(f"\t{file}")

attr = input("What attribute are you interested in? ")

file = open(f"{base_dir}/{attr}")

print(*file)