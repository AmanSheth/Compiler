from syntaxTree import *

def compileFull(expr):
    asm = "global _entry \nsection .text \n_entry: \n"
    asm = compile(asm, expr)
    asm += "ret" 
    with open("output.s", "w") as out_file:
        out_file.write(asm)
    
def compile(asm, expr):
    match(expr): 
        case Integer(): 
            return asm + ("mov rax," + str(expr.val) + "\n")
        case _: 
            raise ValueError("Undefined Value")
