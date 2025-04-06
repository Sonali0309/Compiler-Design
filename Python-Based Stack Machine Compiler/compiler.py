import re

# Token specification
token_specification = [
    ('NUMBER',   r'\d+'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('TIMES',    r'\*'),
    ('DIVIDE',   r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('CUSTOM',   r'%%'),   # <--- Add this line
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)


def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value)))
        elif kind in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'CUSTOM'):  # ✅ FIXED
            tokens.append((kind, value))
        elif kind == 'SKIP':
            continue
        else:
            raise SyntaxError(f"Unexpected character {value}")
    return tokens


class ASTNode:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

class CodeGenerator:
    def __init__(self):
        self.instructions = []

    def generate(self, node):
        if node.type == 'NUM':
            self.instructions.append(f'PUSH {node.value}')
        else:
            self.generate(node.left)
            self.generate(node.right)
            if node.type == 'ADD':
                self.instructions.append('ADD')
            elif node.type == 'SUB':
                self.instructions.append('SUB')
            elif node.type == 'MUL':
                self.instructions.append('MUL')
            elif node.type == 'DIV':
                self.instructions.append('DIV')
        return self.instructions


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        if self.peek() and self.peek()[0] == token_type:
            tok = self.tokens[self.pos]
            self.pos += 1
            return tok
        raise Exception(f"Expected {token_type}, got {self.peek()}")

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()
        while self.peek() and self.peek()[0] in ('PLUS', 'MINUS'):
            if self.peek()[0] == 'PLUS':
                self.eat('PLUS')
                node = ASTNode('ADD', left=node, right=self.term())
            else:
                self.eat('MINUS')
                node = ASTNode('SUB', left=node, right=self.term())
        return node


    def term(self):
        node = self.factor()
        while self.peek() and self.peek()[0] in ('TIMES', 'DIVIDE', 'CUSTOM'):  # ✅ Fix added
            if self.peek()[0] == 'TIMES':
                self.eat('TIMES')
                node = ASTNode('MUL', left=node, right=self.factor())
            elif self.peek()[0] == 'DIVIDE':
                self.eat('DIVIDE')
                node = ASTNode('DIV', left=node, right=self.factor())
            elif self.peek()[0] == 'CUSTOM':
                self.eat('CUSTOM')
                node = ASTNode('CUSTOM_OP', left=node, right=self.factor())
        return node



    def factor(self):
        if self.peek()[0] == 'NUMBER':
            value = self.eat('NUMBER')[1]
            return ASTNode('NUM', value=value)
        elif self.peek()[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        elif self.peek()[0] == 'MINUS':
            self.eat('MINUS')
            return ASTNode('NEG', right=self.factor())
        else:
            raise Exception(f"Unexpected token: {self.peek()}")

tokens = tokenize("2 + 3 * (4 - 1)")
parser = Parser(tokens)
ast = parser.parse()

def print_ast(node, indent=0):
    print('  ' * indent + node.type + (f": {node.value}" if node.value is not None else ""))
    if node.left: print_ast(node.left, indent + 1)
    if node.right: print_ast(node.right, indent + 1)

print_ast(ast)

def generate_code(node):
    if node.type == 'NUM':
        return [f"PUSH {node.value}"]
    elif node.type == 'ADD':
        return generate_code(node.left) + generate_code(node.right) + ["ADD"]
    elif node.type == 'SUB':
        return generate_code(node.left) + generate_code(node.right) + ["SUB"]
    elif node.type == 'MUL':
        return generate_code(node.left) + generate_code(node.right) + ["MUL"]
    elif node.type == 'DIV':
        return generate_code(node.left) + generate_code(node.right) + ["DIV"]
    elif node.type == 'CUSTOM_OP':
        return generate_code(node.left) + generate_code(node.right) + ["CUSTOM"]

code = generate_code(ast)
print("\nAssembly-like Code:")
for instr in code:
    print(instr)


class CodeGenerator:
    def __init__(self):
        self.instructions = []

    def generate(self, node):
        if node.type == 'NUM':
            self.instructions.append(f"PUSH {node.value}")
        else:
            self.generate(node.left)
            self.generate(node.right)
            if node.type == 'ADD':
                self.instructions.append("ADD")
            elif node.type == 'SUB':
                self.instructions.append("SUB")
            elif node.type == 'MUL':
                self.instructions.append("MUL")
            elif node.type == 'DIV':
                self.instructions.append("DIV")
        return self.instructions

# Stack-based virtual machine to execute
def execute(instructions):
    stack = []
    for instr in instructions:
        if instr.startswith("PUSH"):
            _, value = instr.split()
            stack.append(int(value))
        else:
            b = stack.pop()
            a = stack.pop()
            if instr == "ADD":
                stack.append(a + b)
            elif instr == "SUB":
                stack.append(a - b)
            elif instr == "MUL":
                stack.append(a * b)
            elif instr == "DIV":
                stack.append(a // b)
            elif instr == "CUSTOM":
                stack.append(a * a + b * b + a + b + 1)
    return stack[0]


# Code generation
codegen = CodeGenerator()
instructions = codegen.generate(ast)
print("Assembly Instructions:")
for instr in instructions:
    print(instr)

# Execution
result = execute(instructions)
print("Result:", result)

if __name__ == "__main__":
    tokens = tokenize("2 %% 3")
    parser = Parser(tokens)
    ast = parser.parse()
    print_ast(ast)

    code = generate_code(ast)
    print("\nAssembly-like Code:")
    for instr in code:
        print(instr)

    result = execute(code)
    print("Result of 2 %% 3 is:", result)
