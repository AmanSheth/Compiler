miniRack is a toy language! I'm writing a compiler and interpreter in Python 3, to x86 assembly. The functionality of this language is based mostly off Racket, with some variance thrown in for fun! \n
It is dynamically typed and functional. \n

How to use: \n
  The tokenize function (located in tokenizeToMeta.py) takes a piece of miniRack code and tokenizes it into its components. This list of tokens is used as input for the parser. 
  The parse function (located in parse.py) converts a list of tokens into an intermediary meta language, that can be pushed into either the interpreter or the compiler. 
  The interpret function (located in interpreter.py) leverages Python 3 to evaluate a miniRack expression. 
  The compile function (located in compiler.py) converts the meta language representation of a miniRack expression to x86 Assembly (pushed to a file called "output.s"). 
  
  
Expressions: 
  Literals (Dynamically Typed):
    Integers (Version 1.0): miniRack can now handle integers [-2^63: 2^63-1]. 
