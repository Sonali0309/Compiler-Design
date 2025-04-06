# Compiler-Design
Crearting a Virtual Compiler with Custom Operator 

Simple Stack-Based Compiler in Python

This project is a simple stack-based compiler written in Python that performs the full compilation pipeline:

- Lexical Analysis (Tokenization)
- Parsing (Generates an Abstract Syntax Tree)
- Code Generation (Assembly-like instructions)
- Execution (via a custom stack-based virtual machine)

It also includes a **custom operator `%%`** that computes the expression: 
x %% y → x² + y² + x + y + 1

---

## Features

- Arithmetic support: `+`, `-`, `*`, `/`
- Parentheses handling
- Custom operator: `%%`
- Stack-based assembly-like code generation
- Virtual machine to execute compiled instructions

---

## Example

Input Expression:
2 + 3 * (4 - 1)


Generated AST:

ADD
  NUM: 2
  MUL
    NUM: 3
    SUB
      NUM: 4
      NUM: 1


Assembly Code:

PUSH 2
PUSH 3
PUSH 4
PUSH 1
SUB
MUL
ADD

Result: 11

Input with Custom Operator:

2 %% 3


Generated AST:

CUSTOM_OP
  NUM: 2
  NUM: 3

Assembly Code:

PUSH 2
PUSH 3
CUSTOM

Result: 19


---

## How It Works

1. **Tokenizer:** Breaks input into tokens like `NUMBER`, `PLUS`, `CUSTOM`, etc.
2. **Parser:** Converts tokens into an AST based on operator precedence.
3. **Code Generator:** Converts AST into a list of assembly-like instructions.
4. **Executor:** Runs those instructions on a virtual stack machine.

---

## Folder Structure

```
simple_compiler/
├── compiler.py       # Main script
├── README.md         # You’re here!
```

---

## How to Run

bash
python compiler.py

Edit the `expr = "..."` line near the bottom of `compiler.py` to test different expressions.

---

## Requirements

- Python 3.x
- No external libraries needed

---

