import re, pprint, math
from collections import Counter, defaultdict
from itertools import chain

pp = pprint.PrettyPrinter(indent=2)

# Map of element to ingredients (10, A): [(10, ORE)]
elements = defaultdict(list)
for line in open('input.txt', 'r').readlines():
  split = line.strip().split('=>')
  element = re.findall('(\d+) (\w+)', split[1])[0]
  ingredients = [re.findall('(\d+) (\w+)', i)[0] for i in split[0].split(',')]
  elements[element] = ingredients

pp.pprint(elements)

def get_raw_amounts(element, amount, elements_needed, leftovers):
  valid_leftovers = filter(lambda e: e[1] == element, leftovers)
  for l in valid_leftovers:
    amount -= l[0]
    leftovers.remove(l)
  element_key = list((filter(lambda e: e[1] == element, elements)))[0]
  element_requirements = elements[element_key]
  if len(element_requirements) == 1 and element_requirements[0][1] == 'ORE':
    elements_needed.append((amount, element))
  else:
    amounts_multiplier = math.ceil(amount / int(element_key[0]))
    leftover = (amounts_multiplier * int(element_key[0])) - amount
    if leftover > 0:
      leftovers.append((leftover, element))
    for req in element_requirements:
      elements_needed = get_raw_amounts(req[1], amounts_multiplier * int(req[0]), elements_needed, leftovers)
  return elements_needed

ore_needed = 0
fuel_requested = 3343000
while ore_needed < 1000000000000:
  fuel_requested += 1
  needed = [(int(x[0]), x[1]) for x in get_raw_amounts('FUEL', fuel_requested, [], [])]
  counter = defaultdict(int)
  for (amount, element) in needed:
    counter[element] += amount
  ore_needed_total = 0
  for element, amount_needed in counter.items():
    key = list(filter(lambda k: k[1] == element, elements.keys()))[0]
    multiplier = math.ceil(amount_needed / int(key[0]))
    ore_created = int(elements[key][0][0])

    ore_needed_total += multiplier * ore_created

  ore_needed = ore_needed_total

print(fuel_requested)
