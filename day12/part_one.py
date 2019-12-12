import pprint, re
from itertools import combinations
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

def parse_moons():
  moons = {}
  for line in open('input.txt', 'r').readlines():
    matches = tuple(map(int, re.findall('-?\d+', line)))
    moons[matches] = [0,0,0]
  return moons

moons = parse_moons()

def perform_step(moons):
  # First update velocity using gravity
  for moon, current_velocity in moons.items():
    neighbours = [m for m in moons.keys() if m != moon]
    for n in neighbours:
      for i in range(3):
        if n[i] > moon[i]:
          current_velocity[i] += 1
        elif n[i] < moon[i]:
          current_velocity[i] -= 1

  new_moons = {}
  for pos, velocity in moons.items():
    new_pos = tuple([sum(x) for x in zip(pos, velocity)])
    new_moons[new_pos] = velocity
  
  return new_moons

for _ in range(1000):
  moons = perform_step(moons)

total_energy = 0

for pos, vel in moons.items():
  total_energy += sum(map(abs, pos)) * sum(map(abs, vel))

print(total_energy)