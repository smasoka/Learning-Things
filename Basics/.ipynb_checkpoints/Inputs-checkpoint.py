import argparse 
import os

parser = argparse.ArgumentParser()
parser.add_argument("ms", help="Input Measurement Set (MS)")
parser.add_argument("out_ms", help="Output Measurement Set (MS)")
args = parser.parse_args()
print(args.ms)
print(args.out_ms)
os.system(args.ms)