from syntaxTree import *
def intepret(expr):
    match(expr):
        case Integer():
            return expr.val
        case PlusOne():
            return 1 + intepret(expr.target)
        case _:
            return ValueError