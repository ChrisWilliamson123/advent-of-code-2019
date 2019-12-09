from intcode_computer import IntcodeComputer

intcode = open('input.txt', 'r').read().split(',')
intcode = map(int, intcode)
part_one_computer = IntcodeComputer(intcode[:], [1])
part_one_computer.run_program()
print(part_one_computer.outputs[0])
part_two_computer = IntcodeComputer(intcode[:], [2])
part_two_computer.run_program()
print(part_two_computer.outputs[0])

