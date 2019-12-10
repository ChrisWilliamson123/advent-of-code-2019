from math import sqrt, atan, degrees

def get_asteroid_coords(input_rows):
  asteroid_coords = set()
  for y in range(len(input_rows)):
    for x in range(len(input_rows[y])):
      if input_rows[y][x] == '#':
        asteroid_coords.add((x, y))
  return asteroid_coords

# Returns a list of neighbours in the format [neighbour_coord, distance, angle]
def get_neighbours(home_coord, asteroid_coords):
  surrounding = asteroid_coords - {home_coord}
  neighbours = []
  for neighbour in surrounding:
    x_difference = float(neighbour[0] - home_coord[0])
    y_difference = float(neighbour[1] - home_coord[1])
    distance = sqrt(x_difference**2 + y_difference**2)

    if x_difference == 0:
      angle = 180 if y_difference > 0 else 0
    elif y_difference == 0:
      angle = 90 if x_difference > 0 else 270
    else:
      angle = degrees(atan(x_difference/y_difference)) * -1
      
      if y_difference > 0:
        angle += 180

      if angle < 0:
        angle += 360
    if home_coord == (8, 3):
      print(neighbour, angle)
    neighbours.append([neighbour, distance, angle])
  return neighbours

input_rows = [list(l.rstrip()) for l in open('input.txt', 'r').readlines()]

asteroid_coords = get_asteroid_coords(input_rows)

amount_of_viewable_neighbours = []
for asteroid in asteroid_coords:
  neighbours = get_neighbours(asteroid, asteroid_coords)
  amount_of_viewable_neighbours.append((asteroid, len(set(map(lambda n: n[2], neighbours)))))

best_option = max(amount_of_viewable_neighbours, key=lambda x: x[1])
print(best_option[1])

base_station = best_option[0]

neighbours = get_neighbours(base_station, asteroid_coords)

destroyed = []
while len(neighbours) > 0:
  angles = list(set(map(lambda n: n[2], neighbours)))
  angles.sort()

  for angle in angles:
    closest_neighbour_at_angle = min(filter(lambda n: n[2] == angle, neighbours), key=lambda n: n[1])
    neighbours.remove(closest_neighbour_at_angle)
    destroyed.append(closest_neighbour_at_angle)

print(destroyed[199][0][0]*100 + destroyed[199][0][1])
