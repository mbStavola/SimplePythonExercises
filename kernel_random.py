import sys

byte_size = int(sys.argv[1]) if len(sys.argv) > 1 else 1

random_file = open("/dev/urandom", "rb")
random_bytes = random_file.read(byte_size)

number = int.from_bytes(random_bytes, "big")

print(number)