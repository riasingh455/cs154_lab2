# ucsbcs154lab2
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited
import pyrtl
# instantiate a memory block that has our sample instructions stored in it
# translate the following instructions from decimal to MIPS assembly and place in
#decoded.txt for part 1 (c)
sample_instructions = [287965187, 201326593, 2381053956, 6301728]
mem = pyrtl.RomBlock(bitwidth=32, addrwidth=2, romdata=sample_instructions,
max_read_ports=1)
# variable counter will serve as an address in this example
counter = pyrtl.Register(bitwidth=2)
counter.next <<= counter + 1
# read data stored in rom
data = pyrtl.WireVector(bitwidth=32, name='data')
data <<= mem[counter]
# output data
op = pyrtl.Output(bitwidth=6, name='op')
rs = pyrtl.Output(bitwidth=5, name='rs')
rt = pyrtl.Output(bitwidth=5, name='rt')
rd = pyrtl.Output(bitwidth=5, name='rd')
sh = pyrtl.Output(bitwidth=5, name='sh')
func = pyrtl.Output(bitwidth=6, name='func')
imm = pyrtl.Output(bitwidth=16, name='imm')
addr = pyrtl.Output(bitwidth=26, name='addr')
### ADD YOUR INSTRUCTION DECODE LOGIC HERE ###
op <<= data[26:32]      
rs <<= data[21:26]      
rt <<= data[16:21]     
rd <<= data[11:16]      
sh <<= data[6:11]     
func <<= data[0:6]     
imm <<= data[0:16]     
addr <<= data[0:26] 
# simulate
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(4):
    sim.step({})
sim_trace.render_trace(symbol_len=20, segment_size=1)
