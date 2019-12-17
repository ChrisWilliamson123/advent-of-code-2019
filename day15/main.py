import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import defaultdict

class Node:
  def __init__(self, position):
    self.position = position
    self.children = [None, None, None]
    
DIRECTION_MAP = {
  1: [4, 3, 1, 2],
  2: [3, 4, 2, 1],
  3: [1, 2, 3, 4],
  4: [2, 1, 4, 3]
}

DIRECTION_MODIFIERS = {
  1: (0, 1),
  2: (0, -1),
  3: (-1, 0),
  4: (1, 0)
}

OXYGEN_POS = ()
OXYGEN_DEPTH = 0

def wait_for_output(computer):
  current_output = computer.outputs[:]
  while computer.outputs == current_output:
    computer.perform_next_operation()

def modify_position(pos, direction):
  modifier = DIRECTION_MODIFIERS[direction]
  return (pos[0] + modifier[0], pos[1] + modifier[1])

def traverse(root, direction, depth=0):
  global OXYGEN_POS, OXYGEN_DEPTH
  for i in range(3):
    new_direction = DIRECTION_MAP[direction][i]
    computer.inputs.append(new_direction)
    wait_for_output(computer)
    output = computer.outputs[-1]
    new_pos = modify_position(root.position, new_direction)
    if output == 1 or output == 2:
      floor.add(new_pos)
      root.children[i] = Node(new_pos)
      traverse(root.children[i], new_direction, depth + 1)
      if output == 2:
        OXYGEN_POS = new_pos
        OXYGEN_DEPTH = depth + 1
    else:
      walls.add(new_pos)
      root.children[i] = False

  back_direction = DIRECTION_MAP[direction][3]
  computer.inputs.append(back_direction)
  wait_for_output(computer)
  output = computer.outputs[-1]
  next_pos = modify_position(root.position, back_direction)

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

computer = IntcodeComputer(intcode[:], [])
pos = (0,0)
root = Node(pos)

walls = set()
floor = set()
floor.add(pos)

traverse(root, 1)

print(OXYGEN_DEPTH)

oxygen_filled = {OXYGEN_POS}
just_filled = {OXYGEN_POS}
count = 0
while len(oxygen_filled) != len(floor):
  next_filled = set()
  for pos in just_filled:
    neighbours = {
      (pos[0], pos[1]+1),
      (pos[0]+1, pos[1]),
      (pos[0], pos[1]-1),
      (pos[0]-1, pos[1])
    } - walls
    # print(neighbours)
    for n in neighbours:
      oxygen_filled.add(n)
      next_filled.add(n)
  just_filled = next_filled
  count += 1
print(count)
