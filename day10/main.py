from math import sqrt, atan, degrees

input_rows = [list(l.rstrip()) for l in open('input.txt', 'r').readlines()]
# input_rows = [list(l.rstrip()) for l in open('test_input.txt', 'r').readlines()]

asteroid_coords = set()
for y in range(len(input_rows)):
  for x in range(len(input_rows[y])):
    if input_rows[y][x] == '#':
      asteroid_coords.add((x, y))

viewable_neighbours = []
for asteroid in asteroid_coords:
  surrounding = asteroid_coords - {asteroid}
  angles = set()
  for neighbour in surrounding:
    x_difference = float(neighbour[0] - asteroid[0])
    y_difference = float(neighbour[1] - asteroid[1])

    if x_difference == 0:
      if y_difference > 0:
        angle = 180
      else:
        angle = 0
    elif y_difference == 0:
      if x_difference > 0:
        angle = 90
      else:
        angle = 270
    else:
      angle = degrees(atan(float(y_difference)/float(x_difference))) * -1
      
      if y_difference > 0:
        angle += 180
    
    angles.add(angle)

  viewable_neighbours.append(len(angles))

print(max(viewable_neighbours))
