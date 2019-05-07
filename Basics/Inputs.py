#!/anaconda3/bin/python

from sys import argv
import sys
import argparse 

# Using sys library with argv
# Prints a List
print(argv)
for arg in argv:
    print(arg)

print(len(argv))
print("root" in argv)
print("-m" in argv)
print(argv[0])

sys.exit(0)

print("After")
print("\n")    
# Mandatory Arguments
# Dictionary key-value pair
parser = argparse.ArgumentParser()
parser.add_argument("ms", help="Input Measurement Set (MS)")
parser.add_argument("out_ms", help="Output Measurement Set (MS)")

# Optional Arguments
parser.add_argument("-n", "--name", help="Specify the Name of the software")
parser.add_argument("-m", "--mode", help="Specify execution mode")

# Optional Arguments with no value
parser.add_argument("-V", "--version", nargs="?", const="version", help="Displays the software version")
parser.add_argument("-v", "--verbose", nargs="?", const="verbosity", help="Verbosity of of the diagnistics")

args = parser.parse_args()
print(args.ms)
print(args.out_ms)
print(args.name)
print(args.mode)
print(args.verbose)
print(args.version)
print(args)

# if-else to handle this passed arguments
