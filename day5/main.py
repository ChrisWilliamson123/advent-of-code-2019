import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

# Part one
computer = IntcodeComputer(intcode[:], [1])
computer.run_until_halted()
print(computer.outputs[-1])

# Part two
computer = IntcodeComputer(intcode[:], [5])
computer.run_until_halted()
print(computer.outputs[0])