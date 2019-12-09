from intcode_computer import IntcodeComputer

intcode = open('input.txt', 'r').read().split(',')
# intcode = open('test_input.txt', 'r').read().split(',')
intcode = map(int, intcode)
computer = IntcodeComputer(intcode[:], [0])
computer.run_program()
print('Result: {0}'.format(computer.output))
# print(len(str(computer.output)))

