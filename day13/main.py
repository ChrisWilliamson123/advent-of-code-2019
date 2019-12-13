from intcode_computer import IntcodeComputer

intcode = map(int, open('input.txt', 'r').read().split(','))
computer = IntcodeComputer(intcode[:], [])
computer.run_program()
outputs = computer.outputs
grouped_outputs = [outputs[i:i+3] for i in range(0, len(outputs), 3)]
blocks = filter(lambda o: o[2] == 2, grouped_outputs)
part_one = len(blocks)
print(part_one)

intcode[0] = 2
computer = IntcodeComputer(intcode[:], [])
ball_position = (0,0)
paddle_position = (0,0)
previous_output_length = 0
score = 0
while not computer.halted:
  computer.perform_next_operation()
  computer_output_length = len(computer.outputs)
  if previous_output_length != computer_output_length != 0 and computer_output_length % 3 == 0:
    previous_output_length = computer_output_length
    [x, y, tile_type] = computer.outputs[-3:]
    if tile_type == 3:
      paddle_position = (x, y)
    elif tile_type == 4:
      ball_position = (x, y)
      difference = ball_position[0] - paddle_position[0]
      computer.joystick_position = -1 if difference < 0 else 1 if difference > 0 else 0
    elif x == -1 and y == 0:
      score = tile_type

print(score)