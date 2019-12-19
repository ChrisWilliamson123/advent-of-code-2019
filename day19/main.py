import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import Counter

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

affected = set()

max_xs=[]
min_xs = []

def is_tractor_beamed(coord):
  computer = IntcodeComputer(intcode[:], [])
  computer.inputs.append(coord[1])
  computer.inputs.append(coord[0])
  current_outputs = computer.outputs[:]
  while computer.outputs == current_outputs and not computer.halted:
    computer.perform_next_operation()
  return computer.outputs[-1]


# We know from part 1 that len_x ~= y*3
# So if x = 100 y >= 300
y = 750
while True:
  # This x value should be over the length of tractor beam for the selected y value
  x = int(y*2.2)
  tractor_beamed = 0
  while not tractor_beamed:
    x -= 1
    tractor_beamed = is_tractor_beamed((x, y))
  
  # Check the opposite square corner
  if is_tractor_beamed((x-99, y+99)):
    print(((x-99)*10000)+ y)
    exit(1)
  y += 1