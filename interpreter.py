from syntaxTree import *
def intepret(expr):
    match(expr):
        case Integer():
            return expr.val
        case _:
            return ValueError