from tokenizeToMeta import *
from interpreter import *
from compiler import *

print(intepret(tokenize("(++(32))")))

(compileFull(tokenize("(++(32))")))