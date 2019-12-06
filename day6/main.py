from collections import defaultdict

def build_orbital_map(orbits):
  orbital_map = defaultdict(list)
  for k, v in map(lambda o: o.split(')'), orbits):
    orbital_map[k].append(v)
  return orbital_map

def get_edges():
  edges = []
  for node in orbital_map:
    for neighbour in orbital_map[node]:
      edges.append((node, neighbour))
      edges.append((neighbour, node))

  return edges

def get_vertices():
  vertices = set()
  for planet in orbital_map:
    vertices.add(planet)
    for neighbour in orbital_map[planet]:
      vertices.add(neighbour)
  return vertices

def traverse(root, current_depth):
  if len(orbital_map[root]) == 0:
    return current_depth + 1
  else:
    total_depth = 0
    for child in orbital_map[root]:
      total_depth += traverse(child, current_depth + 1)
    return total_depth + current_depth + 1

orbits = [x.rstrip() for x in open('input.txt', 'r').readlines()]
orbital_map = build_orbital_map(orbits)

root = 'COM'

total = traverse(root, -1)
print(total)

unvisited = get_vertices()
all_edges = get_edges()
distances = defaultdict(lambda:1000000)
dest = 'SAN'
current_node = 'YOU'
distances[current_node] = 0

while dest in unvisited:
  neighbours = [e[1] for e in filter(lambda edge: edge[0] == current_node, all_edges)]
  unvisited_neighbours = filter(lambda n: n in unvisited, neighbours)
  for n in unvisited_neighbours:
    neighbour_distance = distances[current_node] + 1
    if neighbour_distance < distances[n]:
      distances[n] = neighbour_distance
  unvisited.remove(current_node)

  current_node = min(unvisited, key=(lambda k: distances[k]))

print(distances[dest]-2)


