import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]
computer = IntcodeComputer(intcode[:], [1])
computer.run_until_halted()
print(computer.outputs[0])

computer = IntcodeComputer(intcode[:], [2])
computer.run_until_halted()
print(computer.outputs[0])
