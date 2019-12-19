from collections import defaultdict

class Node:
  def __init__(self, data):
    self.data = data
    self.children = []

  def __repr__(self):
    return str(self.data)

floor = set()
keys = defaultdict(str)
doors = defaultdict(str)

start_pos = ()
# for y, line in enumerate(open('input.txt', 'r').readlines()):
for y, line in enumerate(open('test_input.txt', 'r').readlines()):  
  for x, char in enumerate(line.strip()):
    pos = (x, y)
    if char == '#':
      continue
    if char == '.':
      floor.add(pos)
    elif char == '@':
      start_pos = pos
      floor.add(pos)
    elif char.isupper() and char.isalpha():
      doors[char] = pos
      floor.add(pos)
    elif char.islower() and char.isalpha():
      keys[char] = pos
      floor.add(pos)



root = Node(start_pos)
print(keys)

def create_tree(root_pos, previous_pos):
  print(root_pos)
  if root_pos in keys.values():
    print('here')
    return root_pos
  elif root_pos in doors.values():
    return None
  else:
    neighbours = {
      (root_pos[0], root_pos[1]+1),
      (root_pos[0]+1, root_pos[1]),
      (root_pos[0], root_pos[1]-1),
      (root_pos[0]-1, root_pos[1]),
    }.intersection(floor) - {previous_pos}
    return [create_tree(n, root_pos) for n in neighbours]

    # for n in neighbours:
    # new_node = Node(n)
    # root.children.append(new_node)
    # create_tree(new_node, root)


tree = create_tree(root.data, root.data)
print(tree)
