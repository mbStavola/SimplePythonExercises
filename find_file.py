import os

files = os.listdir()
search = input("What file are you looking for: ")

matched = []
for file in files:
    match = file.startswith(search)
    if match:
        print(file)