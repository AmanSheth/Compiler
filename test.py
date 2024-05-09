from tokenizeToMeta import *
from parse import *
from interpreter import *
from compiler import *

print(intepret(parse(tokenize("32"))))

(compileFull(parse(tokenize("32"))))