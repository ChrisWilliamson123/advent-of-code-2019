import sys
sys.path.append('..')

from intcode_computer import IntcodeComputer

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

computer = IntcodeComputer(intcode[:], [])

current_outputs = []

open_spaces = set()
scaffolding = set()
robot_pos = ()
robot_direction = ''

output_pos = (0,0)
max_x = 0
while not computer.halted:
  computer.perform_next_operation()
  if computer.outputs != current_outputs:
    latest_output_code = computer.outputs[-1]
    if latest_output_code == 10:
      output_pos = (0, output_pos[1]+1)
    else:
      output_pos = (output_pos[0]+1, output_pos[1])
      max_x = max(max_x, output_pos[0])
      if latest_output_code == 35:
        scaffolding.add(output_pos)
      elif latest_output_code == 46:
        open_spaces.add(output_pos)
      else:
        # It is the robot
        robot_pos = output_pos
        robot_direction = chr(latest_output_code)
    current_outputs = computer.outputs[:]

max_y = output_pos[1]

intersections = set()
for s in scaffolding:
  neighbours = {
    (s[0], s[1]+1),
    (s[0]+1, s[1]),
    (s[0], s[1]-1),
    (s[0]-1, s[1]),
  }.intersection(scaffolding)
  if len(neighbours) == 4:
    intersections.add(s)

alignment_total = 0
for i in intersections:
  alignment_total += (i[0]-1) * (i[1])

print(alignment_total)

intcode_2 = intcode[:]
intcode_2[0] = 2

main_routine = [65,44,65,44,66,44,67,44,66,44,67,44,66,44,67,44,67,44,65,10]
function_a = [82,44,56,44,76,44,52,44,82,44,52,44,82,44,49,48,44,82,44,56,10]
function_b = [76,44,49,50,44,76,44,49,50,44,82,44,56,44,82,44,56,10]
function_c = [82,44,49,48,44,82,44,52,44,82,44,52,10]
video_feed = [110, 10]
computer2 = IntcodeComputer(intcode_2[:], (main_routine + function_a + function_b + function_c + video_feed)[::-1])
computer2.run_until_halted()

print(computer2.outputs[-1])
