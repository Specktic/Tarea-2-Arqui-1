# RISC
def risc_sum_vectors(mem, start_a, start_b, start_res, length):
    instructions = 0
    cycles = 0

    for i in range(length):
        # LOAD A
        val_a = mem[start_a + i][start_a + i]
        instructions += 1
        cycles += 1

        # LOAD B
        val_b = mem[start_b + i][start_b + i]
        instructions += 1
        cycles += 1

        # ADD
        result = val_a + val_b
        instructions += 1
        cycles += 1

        # STORE
        mem[start_res + i] = {start_res + i: result}
        instructions += 1
        cycles += 1

    return mem, instructions, cycles


# Ej
mem = [{i: i} for i in range(10)] + [{10+i: 10+i} for i in range(10)]

start_a, start_b, start_res = 0, 10, 20

# Resultado
mem += [{20+i: 0} for i in range(10)]

mem_risc, instr_risc, cycles_risc = risc_sum_vectors(mem, start_a, start_b, start_res, 10)

print("Resultado RISC:", [list(d.values())[0] for d in mem_risc[start_res:start_res+10]])
print("Instrucciones:", instr_risc, "Ciclos:", cycles_risc)
