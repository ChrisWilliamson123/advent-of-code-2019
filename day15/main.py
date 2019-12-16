import sys, random
sys.path.append('..')

from intcode_computer import IntcodeComputer
from collections import deque, defaultdict

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

# Accept a movement command via an input instruction.
# Send the movement command to the repair droid.
# Wait for the repair droid to finish the movement operation.
# Report on the status of the repair droid via an output instruction.

# 1 North
# 2 South
# 3 West
# 4 East

# 0 Wall
# 1 Moved
# 2 Reached oxygen system

directions = deque([(1, (1, 0)), (4, (0, 1)), (2, (-1, 0)), (3, (0, -1))])

computer = IntcodeComputer(intcode[:], [directions[0][0]])
current_outputs = 0
robot_pos = (0,0)
walls = set()
covered = set()

new_position_delay = 0
oxygen_pos = ()
# covered.add(robot_pos)

while new_position_delay < 1000000:
  computer.perform_next_operation()
  latest_outputs = len(computer.outputs)
  if latest_outputs != current_outputs:
    latest_output = computer.outputs[-1]
    # print('Output: {0}'.format(latest_output))
    if latest_output == 0:
      walls.add((robot_pos[0] + directions[0][1][0], robot_pos[1] + directions[0][1][1]))
      directions.rotate(random.choice([-1, -2, -3]))
      while directions[0] in walls:
        directions.rotate(-1)
      computer.inputs.append(directions[0][0])
      # print('Attempting to move {0}'.format(directions[0][0]))
    elif latest_output == 1:
      # computer.inputs.append(directions[0][0])
      robot_pos = (robot_pos[0] + directions[0][1][0], robot_pos[1] + directions[0][1][1])
      if robot_pos in covered:
        new_position_delay += 1
      else:
        new_position_delay = 0
      covered.add(robot_pos)
      directions.rotate(random.choice([-1, -2, -3]))
      while directions[0] in walls:
        directions.rotate(-1)
      computer.inputs.append(directions[0][0])
      # print(robot_pos)
    else:
      # Found the oxygen
      robot_pos = (robot_pos[0] + directions[0][1][0], robot_pos[1] + directions[0][1][1])
      oxygen_pos = (robot_pos[0] + directions[0][1][0], robot_pos[1] + directions[0][1][1])
      print('found')
      covered.add(robot_pos)
      directions.rotate(random.choice([-1, -2, -3]))
      while directions[0] in walls:
        directions.rotate(-1)
      computer.inputs.append(directions[0][0])
    current_outputs = latest_outputs

# print(robot_pos)
# print(walls)
# print(covered)

min_x = min([min(walls, key=lambda w: w[0]), min(covered, key=lambda c: c[0])])[0]
max_x = max([max(walls, key=lambda w: w[0]), max(covered, key=lambda c: c[0])])[0]

min_y = min([min(walls, key=lambda w: w[1]), min(covered, key=lambda c: c[1])])[1]
max_y = max([max(walls, key=lambda w: w[1]), max(covered, key=lambda c: c[1])])[1]

# print(min_x, min_y)
# print(max_x, max_y)

for y in range(max_y, min_y-1, -1):
  to_print = ''
  for x in range(min_x, max_x+1):
    pos = (x, y)
    # print(pos)
    if pos == (0,0):
      to_print += 'O'
    elif pos in walls:
      to_print += '#'
    elif pos in covered and pos != oxygen_pos:
      to_print += '.'
    elif pos == oxygen_pos:
      to_print += 'D'
    else:
      to_print += u'\u2588'

  print(to_print)


unvisited = covered.copy()
distances = defaultdict(lambda:1000000)
current_node = (0,0)
distances[current_node] = 0
destination = robot_pos

def get_unvisited_neighbours(neighbours, unvisited):
  for n in filter(lambda n: n in unvisited, neighbours):
    yield n

while destination in unvisited:
  # neighbours = [e[1] for e in filter(lambda edge: edge[0] == current_node, all_edges)]
  # print('here')
  neighbours = {
    (current_node[0], current_node[1]+1),
    (current_node[0]+1, current_node[1]),
    (current_node[0], current_node[1]-1),
    (current_node[0]-1, current_node[1])
  }
  neighbours = neighbours - walls
  # print(neighbours)
  unvisited_neighbours = get_unvisited_neighbours(neighbours, unvisited)
  for n in unvisited_neighbours:
    neighbour_distance = distances[current_node] + 1
    if neighbour_distance < distances[n]:
      distances[n] = neighbour_distance
  unvisited.remove(current_node)

  if len(unvisited) > 0:
    current_node = min(unvisited, key=(lambda k: distances[k]))
  else:
    break
print(distances[destination])

max_distance = 0
count = 0
for node in covered:
  unvisited = covered.copy()
  distances = defaultdict(lambda:1000000)
  current_node = robot_pos
  distances[current_node] = 0
  destination = node

  while destination in unvisited:
    # neighbours = [e[1] for e in filter(lambda edge: edge[0] == current_node, all_edges)]
    neighbours = {
      (current_node[0], current_node[1]+1),
      (current_node[0]+1, current_node[1]),
      (current_node[0], current_node[1]-1),
      (current_node[0]-1, current_node[1])
    }
    neighbours = neighbours - walls
    unvisited_neighbours = get_unvisited_neighbours(neighbours, unvisited)
    for n in unvisited_neighbours:
      neighbour_distance = distances[current_node] + 1
      if neighbour_distance < distances[n]:
        distances[n] = neighbour_distance
    unvisited.remove(current_node)

    if len(unvisited) > 0:
      current_node = min(unvisited, key=(lambda k: distances[k]))
    else:
      break
  # print(distances[destination])
  if distances[destination] > max_distance:
    max_distance = distances[destination]
  count += 1
  
  # print('Done {0}/{1}'.format(count, len(covered)))
print(max_distance)

















































# floor = set()
# walls = set()
# o = ()

# max_y = 0
# max_x = 0
# for y, line in enumerate(open('full_grid.txt', 'r').readlines()):
#   max_y = y
#   for x, c in enumerate(line):
#     max_x = x
#     pos = (x, y)
#     # print(pos)
#     if c == '.' or c == 'O':
#       floor.add(pos)
#     elif c == '#':
#       walls.add(pos)
#     elif c == 'D':
#       floor.add(pos)
#       o = pos

# print(o)
# oxygen_filled = {o}
# current = o
# prev_filled = {o}
# time = 0
# while len(oxygen_filled) != len(floor):
#   just_filled = set()
#   for cell in prev_filled:
#     adjacents = filter(
#       lambda c: c not in walls and c not in oxygen_filled,
#       {
#         (cell[0], cell[1]+1),
#         (cell[0]+1, cell[1]),
#         (cell[0], cell[1]-1),
#         (cell[0]-1, cell[1])
#       }
#     )
#     for a in adjacents:
#       oxygen_filled.add(a)
#       just_filled.add(a)
#   time += 1
#   prev_filled = just_filled

#   for y in range(0, max_y+1):
#     to_print = ''
#     for x in range(0, max_x+1):
#       pos = (x,y)
#       if pos in walls:
#         to_print += '#'
#       elif pos in oxygen_filled:
#         to_print += 'O'
#       elif pos in floor:
#         to_print += '.'
#       else:
#         to_print += '\u2588'
#     print(to_print)
#   print('\n\n\n\n\n')

# print(time)