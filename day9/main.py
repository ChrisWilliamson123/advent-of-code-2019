from intcode_computer import IntcodeComputer

intcode = open('input.txt', 'r').read().split(',')
# intcode = open('test_input.txt', 'r').read().split(',')
intcode = map(int, intcode)
computer = IntcodeComputer(intcode[:], [2])
computer.run_program()
print('Result: {0}'.format(computer.outputs))
# print(len(str(computer.output)))

