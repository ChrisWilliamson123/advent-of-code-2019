import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

part_one_intcode = intcode[:]
part_one_intcode[1:3] = [12, 2]
computer = IntcodeComputer(part_one_intcode, [])
computer.run_until_halted()
print(computer.memory[0])

for noun in range(100):
  for verb in range(100):
    ic = intcode[:]
    ic[1:3] = [noun, verb]
    computer = IntcodeComputer(ic, [])
    computer.run_until_halted()
    output = computer.memory[0]
    
    if output == 19690720:
      print(100 * noun + verb)
      exit(0)
