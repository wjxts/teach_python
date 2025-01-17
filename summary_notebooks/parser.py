import argparse

parser = argparse.ArgumentParser(description='test')
parser.add_argument('--foo', help='foo help')
# 默认情况下，它的类型是字符串（str）， 默认default=None
parser.add_argument('--age', type=int, default=0, help="age of the person", required=True)
parser.add_argument('--name', type=str, default="", help="name of the person")
parser.add_argument('--height', type=float, default=1.0, help="height of the person (unit: meter)")
parser.add_argument("--man", action="store_true", help="whether the person is a man")
parser.add_argument("--cousins", nargs="+", help="cousins of the person", choices=['a','b'])
# 3: 3 values, can be any number you want
# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
# 即使不满足也不会报错，只是不会被解析, 都可以是None

parser.add_argument("--sons", nargs=1, help="sons of the person") # list
parser.add_argument("--wife", type=str, nargs="?", help="wife of the person") # single value, not list
parser.add_argument("--model", default="resnet", help="model to use", choices=["resnet", "vgg", "densenet"])
# args = parser.parse_args()
args, unknown = parser.parse_known_args()
print(args, unknown)
print(args.model)