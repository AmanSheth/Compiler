import syntaxTree

def parse(tokens):
    for tok in tokens: 
        match tok: 
            case int():
                return syntaxTree.Integer(tok)
            case _: 
                raise ValueError(tok + " is not a valid expression in miniRack")