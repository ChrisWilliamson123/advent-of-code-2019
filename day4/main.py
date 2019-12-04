range_lower = 146810
range_higher = 612564

def is_valid(number):
  as_string = str(number)
  adjacents = []

  for i in range(1, len(as_string)):
    current = int(as_string[i])
    previous = int(as_string[i-1])
    if current < previous:
      return False

    if current == previous:
      adjacents.append((i, i-1, current))

  # Part one, comment these two lines to get part two answer
  if len(adjacents):
    return True
  
  number_of_adjacents = {}
  for a in adjacents:
    if a[2] in number_of_adjacents:
      number_of_adjacents[a[2]] += 1
    else:
      number_of_adjacents[a[2]] = 1

  # Part two
  if 1 in number_of_adjacents.values():
    return True

total = 0
for i in range(range_lower, range_higher+1):
  if is_valid(i):
    total += 1

print(total)
# print(is_valid(123444))