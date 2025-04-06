# Compiler-Design
Crearting Compilers with Custom Operator 

# Custom Mini Compiler Project

This project contains **two implementations** of a simple compiler:

1. **Python-Based Stack Machine Compiler**
2. **Lex/Yacc-Based Compiler with Assembly Code Generation**

---

## Python-Based Compiler

### Features

- Tokenizes mathematical expressions (supports `+`, `-`, `*`, `/`, and a custom operator `%%`)
- Generates an Abstract Syntax Tree (AST)
- Produces assembly-like code
- Executes the code using a stack-based virtual machine

### Custom Operator `%%`
Implements: `x*x + y*y + x + y + 1`

### Files
- `compiler.py` – Main Python compiler script
- `README.md` – You’re reading it

###  Example Input & Output

Input:
```
2 %% 3
```

Assembly:
```
PUSH 2
PUSH 3
CUSTOM
```

Result: `2*2 + 3*3 + 2 + 3 + 1 = 19`

---

## Lex/Yacc-Based Compiler

### Features

- Lexical analysis using `lexer.l`
- Parsing using `parser.y`
- Handles standard and custom expressions (including `%%`)
- Outputs pseudo-assembly code

###  Custom Operator `%%`
Implemented as a new token and handled in grammar rules and assembly generation.

###  Files
- `lexer.l` – Defines tokens including `%%`
- `parser.y` – Contains grammar rules and code generation logic
- `output.s` – Final assembly-like output file
- `README.md` – You’re reading it

###  Build & Run Instructions

install and set up MSYS2

```bash
flex lexer.l
bison -d parser.y
gcc lex.yy.c parser.tab.c -o compiler
./compiler
```

Enter input like:
```
2 %% 3
```

Assembly output will be in `output.s`

---

Developed as part of a Compiler Design assignment. 


