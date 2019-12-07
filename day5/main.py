from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

# Part one
computer = IntcodeComputer(intcode[:], [1])
computer.run_program()
print(computer.output)

# Part two
computer = IntcodeComputer(intcode[:], [5])
computer.run_program()
print(computer.output)