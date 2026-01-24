import argparse
import random
import string

parser = argparse.ArgumentParser()
parser.add_argument("--length", type=int, default=8)
args = parser.parse_args()

chars = string.ascii_letters + string.digits
words =  []
for _ in range(args.length):
    words.append(random.choice(chars))

password = "".join(words)

print("Password:", password)