import pyrtl
### DECLARE WIRE VECTORS, INPUT, MEMBLOCK ###
### DECODE INSTRUCTION AND RETRIEVE RF DATA ###
### ADD ALU LOGIC HERE ###
### WRITEBACK ###

instr = pyrtl.Input(bitwidth=32, name='instr')
rf = pyrtl.MemBlock(bitwidth=32, addrwidth=5, name='rf') #reg file

rs = instr[21:26]
rt = instr[16:21]
rd = instr[11:16]
shamt = instr[6:11]
funct = instr[0:6]

rs_val = rf[rs]
rt_val = rf[rt]

alu_result = pyrtl.WireVector(bitwidth=32, name='alu_result')


with pyrtl.conditional_assignment:
    with funct == 32:
        alu_result |= rs_val + rt_val #add
    with funct == 34:
        alu_result |= rs_val - rt_val #sub
    with funct == 36:
        alu_result |= rs_val & rt_val #and
    with funct == 37:
        alu_result |= rs_val | rt_val #or
    with funct == 38:
        alu_result |= rs_val ^ rt_val #xor
    with funct == 0:
        alu_result |= rt_val << shamt #sll
    with funct == 2:
        alu_result |= rt_val >> shamt #srl
    with funct == 3:
        alu_result |= pyrtl.shift_right_arithmetic(rt_val, shamt)#sra
    with funct == 42:
        alu_result |= pyrtl.signed_lt(rs_val, rt_val) #slt

#writeback
rf[rd] <<= alu_result