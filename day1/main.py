from math import floor

masses = [int(m.rstrip()) for m in open('input.txt', 'r').readlines()]

def calc_fuel(mass):
  return floor(mass/3)-2

part_one=sum(map(calc_fuel, masses))
print(part_one)

def total_fuel_needed(mass):
  total = 0
  mass = calc_fuel(mass)
  while mass > 0:
    total += mass
    mass = calc_fuel(mass)
  return total

part_two = sum(map(total_fuel_needed, masses))
print(part_two)
