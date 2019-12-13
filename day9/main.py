import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]
part_one_computer = IntcodeComputer(intcode[:], [1])
while not part_one_computer.halted:
  part_one_computer.perform_next_operation()
print(part_one_computer.outputs[0])

part_two_computer = IntcodeComputer(intcode[:], [2])
while not part_two_computer.halted:
  part_two_computer.perform_next_operation()
print(part_two_computer.outputs[0])
