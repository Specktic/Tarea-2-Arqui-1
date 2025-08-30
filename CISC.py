# CISC 
def cisc_sum(mem, start_a, start_b, start_res, length):
    instructions = 0
    cycles = 0

    for i in range(length):
        # SUMMEM
        val_a = mem[start_a + i][start_a + i]
        val_b = mem[start_b + i][start_b + i]
        result = val_a + val_b
        mem[start_res + i] = {start_res + i: result}

        instructions += 1          # SUMMEM
        cycles += 3                # SUMMEM dura 3 ciclos

    return mem, instructions, cycles


# Ej
mem = [{i: i} for i in range(10)] + [{10+i: 10+i} for i in range(10)]

start_a, start_b, start_res = 0, 10, 20

# Resultado
mem += [{20+i: 0} for i in range(10)]

mem_cisc, instr_cisc, cycles_cisc = cisc_sum(mem, start_a, start_b, start_res, 10)

print("Resultado CISC:", [list(d.values())[0] for d in mem_cisc[start_res:start_res+10]])
print("Instrucciones:", instr_cisc, "Ciclos:", cycles_cisc)
