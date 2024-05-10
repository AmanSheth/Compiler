from syntaxTree import *

def compileFull(expr):
    asm = "global _entry \nsection .text \n_entry: \n"
    asm = compile(asm, expr)
    asm += "ret" 
    with open("output.s", "w") as out_file:
        out_file.write(asm)
    
def compile(asm, expr):
    print(expr)
    match(expr): 
        case Integer(): 
            return asm + ("mov rax," + str(expr.val) + "\n")
        
        case PlusOne():
            return asm + compile(asm, expr.target) + ("add rax, 1 \n")
        
        case _: 
            raise ValueError("Undefined Value")
