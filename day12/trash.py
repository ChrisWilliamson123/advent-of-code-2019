# pp.pprint(moons)

steps_to_repeat = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

velocities = [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]

for i, v in enumerate([m[1] for m in moons]):
  for j in range(3):
    velocities[i][j].append(v[j])

pp.pprint(velocities)

for _ in range(100000):
  moons = perform_step(moons)
  for i, v in enumerate([m[1] for m in moons]):
    for j in range(3):
      velocities[i][j].append(v[j])

# pp.pprint(velocities)

for i, v in enumerate(velocities):
  for j, coord_velocities in enumerate(v):
    s = []
    for k in range(1, len(coord_velocities)-1):
      if coord_velocities[0:k+1] == coord_velocities[k+1:(k*2)+2]:
        s.append(coord_velocities[0:k+1])
    # print(s)[0]
    # print(len(s[0]), sum(s[0]))
    # r.append(len(s[0]))
    steps_to_repeat[i][j] = len(s[0])

pp.pprint(steps_to_repeat)
# for j in [x, y, z]:

# print(lcm(r[0], r[1], r[2]))
# x.append(moons[0][1][0])
# y.append(moons[0][1][1])
# z.append(moons[0][1][2])
# for _ in range(100):
#   moons = perform_step(moons)
#   x.append(moons[0][1][0])
#   y.append(moons[0][1][1])
#   z.append(moons[0][1][2])
#   # pp.pprint(moons)
#   print(moons[0][1][0], moons[0][1][1], moons[0][1][2])

# print(x)
# print(y)
# print(z)

# def gcd2(a, b, c):
#   return gcd(a, gcd(b, c))

# def lcm(a, b, c):
#     # return abs(a*b*c) // gcd2(a, b, c)
#     i = max(a, b, c)
#     while True:
#       if i % a == 0 and i % b == 0 and i % c == 0:
#         return i
#       i += 1






# velocity_totals = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# steps = 0
# while 0 in chain(*steps_to_repeat):
#   moons = perform_step(moons)
#   steps += 1
#   velocities = [m[1] for m in moons]
#   for i in range(len(velocity_totals)):
#     for j in range(3):
#       velocity_totals[i][j] +=  velocities[i][j]
#       if velocity_totals[i][j] == 0 and steps_to_repeat[i][j] == 0:
#         steps_to_repeat[i][j] = steps + 1
#         # pp.pprint(steps_to_repeat)
#   pp.pprint(velocity_totals)
# pp.pprint(steps_to_repeat)
    # new_velocity_totals.append(map(operator.add, velocity_totals[i], velocities[i]))

  # velocity_totals = new_velocity_totals

# zipped = zip(velocity_totals, velocities)
# for z in zipped:
#   z = map(operator.add, z[0], z[1])







# # pp.pprint(moons)

# # all_moon_states = set()
# # # all_moon_states[tuple(sorted(moons.keys()))] = sorted(moons.values())

# # # pp.pprint(all_moon_states)

# # def hash_moons(moons):
# #   hash = ''
# #   for pos, vel in sorted(moons.items()):
# #     hash += ''.join(map(str, pos) + map(str, vel))
# #   return hash

# #   # print(combined)

# # moon_hash = hash_moons(moons)

# # steps = 0
# # while moon_hash not in all_moon_states:
# #   all_moon_states.add(moon_hash)
# #   moons = perform_step(moons)
# #   moon_hash = hash_moons(moons)
# #   steps += 1
# #   if steps % 1000 == 0:
# #     print(steps)

# # print(len(all_moon_states))
# # # ordered_moons = tuple(tuple(sorted(moons.keys())) + tuple(map(tuple, sorted(moons.values()))))
# # # print(ordered_moons)
# # # step = 0
# # # while all_moon_states[ordered_moons] == []:
# # #   all_moon_states[ordered_moons] = sorted(moons.values())
# # #   moons = perform_step(moons)
# # #   ordered_moons = tuple(tuple(sorted(moons.keys())) + tuple(map(tuple, sorted(moons.values()))))
# # #   step += 1
# # #   print(step)



  
