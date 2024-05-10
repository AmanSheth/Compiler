from syntaxTree import *
def tokenize(expr):
    match (expr[0]):
        case "(": 
            return tokenizeExpr(expr[1:])
        case _: 
            return TypeError("Invalid Syntax")


def tokenizeExpr(expr):
    match (expr[0]):
        case "(":
            return tokenizeExpr(expr[1:])
        
        case s if s.isdigit():
            return tokenizeInteger(expr)
        
        case s if s == "+":
            if expr[1] == "+":
                return PlusOne(tokenizeExpr(expr[2:]))
            else: 
                return TypeError("Invalid Syntax")
        case _: 
            return TypeError("Invalid Syntax")

def tokenizeInteger(expr):
    i = ""

    for c in expr: 
        if c == ")":
            return Integer(int(i))
        i += c
    
    return TypeError("Invalid Syntax")

