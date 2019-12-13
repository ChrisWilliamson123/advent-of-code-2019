import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import deque, defaultdict

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]
computer = IntcodeComputer(intcode[:], [0])
# Uncomment line below to run part 2
computer = IntcodeComputer(intcode[:], [1])

position = (0,0)
directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
current_direction = directions[0]
painted_tiles = defaultdict(int)
# Uncomment line below to run part 2
painted_tiles[position] = 1
previous_output_length = 0

while not computer.halted:
  computer.perform_next_operation()
  computer_output_length = len(computer.outputs)
  if previous_output_length != computer_output_length != 0 and computer_output_length % 2 == 0:
    previous_output_length = computer_output_length
    [colour, direction] = computer.outputs[-2:]
    painted_tiles[position] = colour
    directions.rotate(-1) if direction == 1 else directions.rotate(1)
    current_direction = directions[0]
    position = (position[0] + current_direction[0], position[1] + current_direction[1])
    computer.inputs.append(painted_tiles[position])
print(len(painted_tiles))

# Uncomment all of this below to run part 2
min_x = min(painted_tiles.keys(), key=lambda p: p[0])[0]
max_x = max(painted_tiles.keys(), key=lambda p: p[0])[0]

min_y = min(painted_tiles.keys(), key=lambda p: p[1])[1]
max_y = max(painted_tiles.keys(), key=lambda p: p[1])[1]

for y in range(max_y, min_y-1, -1):
  to_print = ''
  for x in range(min_x, max_x + 1):
    if (x, y) in painted_tiles:
      if painted_tiles[(x, y)] == 1:
        to_print += '#'
      else:
        to_print += ' '
    else:
      to_print += ' '
  print(to_print)
