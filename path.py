# import os 

# file_list = os.listdir(".")
# # print(file_list)
# # os.makedirs("test_dir")
# # print(os.__file__)
# py_file = [file for file in file_list if file.endswith(".py")]
# print(py_file)


# import glob 

# py_file2 = glob.glob("*.py")
# print(py_file2)


# from pathlib import Path

# path = Path(".")
# print(path)
# math_path = path / "new_math" / "op.py"
# print(math_path)

# base_path = ""
# file1 = base_path / "xxx1"
# file2 = base_path / "xxx2"

# import os 
# s = os.system("python hw1.py")
# s = os.popen("python hw1.py").read()
# print(s)

# from recursion import fib
# import sys
# #print(sys.argv) #CLI
# args = sys.argv

# n = int(args[1])
# print(fib(n))

from recursion import fib
import argparse
parser = argparse.ArgumentParser(description="learn")
parser.add_argument("--n", type=int, default=10, help="input of fib")
args = parser.parse_args()

print(fib(args.n))

