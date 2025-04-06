def compile_custom_expr(a, b):
    asm = []
    asm.append(f"MOV R1, {a}")
    asm.append("IMUL R1, R1")          # R1 = a * a
    asm.append(f"MOV R2, {b}")
    asm.append("IMUL R2, R2")          # R2 = b * b
    asm.append("ADD R1, R2")           # R1 = a^2 + b^2
    asm.append(f"ADD R1, {a}")         # + a
    asm.append(f"ADD R1, {b}")         # + b
    asm.append("ADD R1, 1")            # + 1
    return asm

a = int(input("Enter a: "))
b = int(input("Enter b: "))

assembly = compile_custom_expr(a, b)
print("\n".join(assembly))
