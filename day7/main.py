import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer
from itertools import permutations
from collections import deque

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

max_power_output = 0
for phases in permutations([0, 1, 2, 3, 4]):
  latest_amp_output = 0
  for i in range(5):
    computer = IntcodeComputer(intcode[:], [latest_amp_output, phases[i]])
    outputs = computer.outputs
    while len(outputs) == 0:
      computer.perform_next_operation()
    latest_amp_output = computer.outputs[0]
  if latest_amp_output > max_power_output:
    max_power_output = latest_amp_output

print(max_power_output)

max_power = 0
for phases in permutations([5, 6, 7, 8, 9]):
  amps = deque([
    IntcodeComputer(intcode[:], [0, phases[0]]),
    IntcodeComputer(intcode[:], [phases[1]]),
    IntcodeComputer(intcode[:], [phases[2]]),
    IntcodeComputer(intcode[:], [phases[3]]),
    IntcodeComputer(intcode[:], [phases[4]]),
  ])
  current_amp = amps[0]
  latest_output = 0
  while not current_amp.halted:
    current_output = current_amp.outputs[:]
    while current_output == current_amp.outputs and not current_amp.halted:
      current_amp.perform_next_operation()
    latest_output = current_amp.outputs[-1]
    amps[1].inputs.insert(0, latest_output)
    amps.rotate(-1)
    current_amp = amps[0]
  if latest_output > max_power:
    max_power = latest_output
print(max_power)
    