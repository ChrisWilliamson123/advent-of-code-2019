import sys, random
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import deque, defaultdict

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

# NORTH_DIRECTIONS = [
#   (4, (0, 1)),
#   (2, (-1, 0)),
#   (1, (1, 0)),
#   (3, (0, -1))
# ]

# 1 N
# 2 S
# 3 W
# 4 E

directions = [
  (4, (1, 0)),
  (3, (-1, 0)),
  (1, (0, 1)),
  (2, (0, -1)),
]
print(directions)
# Facing east (S, N, E, W) (2, 1, 4, 3)
# Facing south (W, E, S, N) (3, 4, 2, 1)

# directions = deque([
#   (3, (0, -1))
#   (4, (0, 1)),
#   (2, (-1, 0)),
#   (1, (1, 0)),
# ])

def turn_right(directions):
  return [directions[3], directions[2], directions[0], directions[1]]

def turn_left(directions):
  return [directions[2], directions[3], directions[1], directions[0]]

computer = IntcodeComputer(intcode[:], [directions[0][0]])

current_outputs = 0
robot_pos = (0,0)
walls = set()
covered = set()

while True:
  computer.perform_next_operation()
  latest_outputs = len(computer.outputs)
  if latest_outputs != current_outputs:
    # Add the position the walls
    walls.add((robot_pos[0] + directions[0][1][0], robot_pos[1] + directions[0][1][1]))
    directions.rotate(-1)
    computer.inputs.append(directions[0][0])