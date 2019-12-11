from intcode_computer import IntcodeComputer

intcode = map(int, open('input.txt', 'r').read().split(','))
# print(intcode)

computer = IntcodeComputer(intcode[:], [0])

computer.run_program()

painted_positions = computer.painted_tiles.keys()

print(painted_positions)

min_x = min(painted_positions, key=lambda p: p[0])[0]
max_x = max(painted_positions, key=lambda p: p[0])[0]

min_y = min(painted_positions, key=lambda p: p[1])[1]
max_y = max(painted_positions, key=lambda p: p[1])[1]

print(min_x, min_y)
print(max_x, max_y)

for y in range(min_y, max_y + 1):
  to_print = ''
  for x in range(min_x, max_x + 1):
    if (x, y) in computer.painted_tiles:
      if computer.painted_tiles[(x, y)] == 1:
        to_print += '#'
      else:
        to_print += ' '
    else:
      to_print += ' '
  print(to_print)