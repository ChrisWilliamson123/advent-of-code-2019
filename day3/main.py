wires = [x.rstrip() for x in open('input.txt', 'r').readlines()]

def manhattan_distance(pos1, pos2):
  return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

all_coords_hit = []

for wire in wires:
  wire_coords = []

  current_pos = (0,0)
  move_generator = (move for move in wire.split(','))
  
  for move in move_generator:
    direction = move[0]
    amount = int(move[1:])

    if direction == 'U':
      for x in range(1, amount+1):
        wire_coords.append((current_pos[0], current_pos[1] + x))
    elif direction == 'D':
      for x in range(1, amount+1):
        wire_coords.append((current_pos[0], current_pos[1] - x))
    elif direction == 'L':
      for x in range(1, amount+1):
        wire_coords.append((current_pos[0] - x, current_pos[1]))
    else:
      for x in range(1, amount+1):
        wire_coords.append((current_pos[0] + x, current_pos[1]))

    current_pos = wire_coords[-1]

  all_coords_hit.append(wire_coords)

intersection_coords = set(all_coords_hit[0]).intersection(set(all_coords_hit[1]))

distances = map(lambda i: manhattan_distance(i, (0,0)), intersection_coords)

part_one = min(distances)
print(part_one)

times_to_reach_intersections = []
for i in intersection_coords:
  first_wire_index = 0
  while all_coords_hit[0][first_wire_index] != i:
    first_wire_index += 1
  first_wire_index += 1

  second_wire_index = 0
  while all_coords_hit[1][second_wire_index] != i:
    second_wire_index += 1
  second_wire_index += 1

  times_to_reach_intersections.append(first_wire_index + second_wire_index)

part_two = min(times_to_reach_intersections)
print(part_two)
