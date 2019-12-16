import sys, random
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import deque, defaultdict

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

DIRECTION_MAP = {
  1: [4, 3, 2],
  2: [2, 1, 3],
  3: [3, 4, 1],
  4: [1, 3, 4]
}

DIRECTION_MODIFIERS = {
  1: (0, 1),
  2: (0, -1),
  3: (-1, 0),
  4: (1, 0)
}

class Node:
  def __init__(self, position):
    self.position = position
    self.children = []

# 1, 4, 2, 3
# N, E, S, W
current_node = Node((0,0))
current_direction = 1
computer = IntcodeComputer(intcode[:], [])

def build_tree(root, direction):

  # Go right
  next_direction = DIRECTION_MAP[direction][0]
  computer.inputs.append(next_direction)
  latest_outputs = []
  while computer.outputs == latest_outputs:
    computer.perform_next_operation()
  latest_output = computer.outputs[-1]
  latest_outputs = computer.outputs[:]
  print('Right output: {0}'.format(latest_output))

  if latest_output == 1:
    modifier = DIRECTION_MODIFIERS[next_direction]
    right_node = Node((current_node.position[0] + modifier[0], current_node.position[1] + modifier[1]))
    current_node.children.append(right_node)
    build_tree(right_node, next_direction)
  
  # Go forward
  computer.inputs.append(direction)
  while computer.outputs == latest_outputs:
    computer.perform_next_operation()
  latest_output = computer.outputs[-1]
  latest_outputs = computer.outputs[:]
  print('Forward output: {0}'.format(latest_output))

  if latest_output == 1:
    modifier = DIRECTION_MODIFIERS[direction]
    forward_node = Node((current_node.position[0] + modifier[0], current_node.position[1] + modifier[1]))
    current_node.children.append(forward_node)
    build_tree(forward_node, direction)

  # Go left
  next_direction = DIRECTION_MAP[direction][1]
  computer.inputs.append(next_direction)
  while computer.outputs == latest_outputs:
    computer.perform_next_operation()
  latest_output = computer.outputs[-1]
  latest_outputs = computer.outputs[:]
  print('Left output: {0}'.format(latest_output))

  if latest_output == 1:
    modifier = DIRECTION_MODIFIERS[next_direction]
    right_node = Node((current_node.position[0] + modifier[0], current_node.position[1] + modifier[1]))
    current_node.children.append(right_node)
    build_tree(right_node, next_direction)

build_tree(current_node, current_direction)



# def build_tree(root, direction):
#   # Check the right node

