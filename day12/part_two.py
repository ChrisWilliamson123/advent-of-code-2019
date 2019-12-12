import re

def parse_moons():
  moons = []
  for line in open('input.txt', 'r').readlines():
    matches = tuple(map(int, re.findall('-?\d+', line)))
    moons.append({
      'position': matches,
      'velocity': [0,0,0]
    })
  return moons

def move_coord(pos, vel, other_positions):
  for p in other_positions:
    if p > pos:
      vel += 1
    elif p < pos:
      vel -= 1

  return (pos + vel, vel)

def gcd(a,b):
  """Compute the greatest common divisor of a and b"""
  while b > 0:
    a, b = b, a % b
  return a
    
def lcm(a, b):
  """Compute the lowest common multiple of a and b"""
  return a * b / gcd(a, b)

moons = parse_moons()

steps_needed = []
for i in range(3):
  original_states = []
  for m in moons:
    original_states.append((m['position'][i], m['velocity'][i]))

  current_states = original_states[:]

  next_states = []
  for s in current_states:
    next_states.append(move_coord(s[0], s[1], [o[0] for o in [p for p in current_states if p != s]]))
  current_states = next_states
  steps = 1
  while current_states != original_states:
    next_states = []
    for s in current_states:
      next_states.append(move_coord(s[0], s[1], [o[0] for o in [p for p in current_states if p != s]]))
    current_states = next_states
    steps += 1
  steps_needed.append(steps)

print(lcm(steps_needed[0], lcm(steps_needed[1], steps_needed[2])))