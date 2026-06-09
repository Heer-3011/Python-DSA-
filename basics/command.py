import sys ,argparse
# print(len(sys.argv))
# print("Script name:", sys.argv[0])
# print("Arguments:", sys.argv[1])

parser = argparse.ArgumentParser()
parser.add_argument("--name")
parser.add_argument("--age")
args = parser.parse_args()
print("Hello", args.name,"your age=",args.age)