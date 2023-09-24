filename = input("What file do you want to print? ")

file = open(filename)

for line in file:
    print(line.replace("\n", ""))