from intcode_computer import IntcodeComputer
from itertools import permutations

def get_power_for_phase_set(intcode, phase_set):
  latest_amp_output = 0
  for i in range(5):
    intcode_computer = IntcodeComputer(intcode, [phase_set[i], latest_amp_output])
    intcode_computer.run_program()
    latest_amp_output = intcode_computer.output
  return latest_amp_output

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]
# intcode = [int(x) for x in open('test_input.txt', 'r').read().split(',')]

phase_permutations = list(permutations([0, 1, 2, 3, 4]))

power_outputs = map(lambda phase_set: get_power_for_phase_set(intcode[:], phase_set), phase_permutations)

print(max(power_outputs))

# class Amplifier:
#   def __init__(self, intcode, phase, first = False):
#     self.intcode = intcode
#     self.phase = phase
#     self.instruction_pointer = 0
#     self.inputs = [phase]
#     if first:
#       self.inputs.append(0)
#     self.output = 0

#   def run(self):
#     operation_spec = parse_operation_spec(self.intcode[self.instruction_pointer])
#     while operation_spec[0] != 99:
#       opcode = operation_spec[0]
#       parameter_modes = operation_spec[1]
#       param1_mode = parameter_modes[0]
#       param2_mode = parameter_modes[1]

#       # Addition
#       if opcode == 1:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         destination_address = self.intcode[self.instruction_pointer+3]
#         op_add(self.intcode, value1, value2, destination_address)
#       # Multiplication
#       elif opcode == 2:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         destination_address = self.intcode[self.instruction_pointer+3]
#         op_mul(self.intcode, value1, value2, destination_address)
#       # Input
#       elif opcode == 3:
#         op_input(self.intcode, self.inputs[0], self.intcode[self.instruction_pointer+1])
#         self.inputs.pop(0)
#       # Output
#       elif opcode == 4:
#         if param1_mode == 1:
#           self.output = self.intcode[self.instruction_pointer+1]
#         else:
#           self.output = self.intcode[self.intcode[self.instruction_pointer+1]]
#         self.instruction_pointer += skip_ahead_amount(opcode)
#         return 0
#       # Jump-if-true
#       elif opcode == 5:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         if value1 != 0:
#           self.instruction_pointer = value2
#         else:
#           self.instruction_pointer += 3
#       # Jump-if-false
#       elif opcode == 6:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         if value1 == 0:
#           self.instruction_pointer = value2
#         else:
#           self.instruction_pointer += 3
#       # Less than
#       elif opcode == 7:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         to_store = 0
#         if value1 < value2:
#           to_store = 1
#         self.intcode[self.intcode[self.instruction_pointer+3]] = to_store
#       # Equals
#       elif opcode == 8:
#         (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
#         to_store = 0
#         if value1 == value2:
#           to_store = 1
#         self.intcode[self.intcode[self.instruction_pointer+3]] = to_store

#       self.instruction_pointer += skip_ahead_amount(opcode)
#       operation_spec = parse_operation_spec(self.intcode[self.instruction_pointer])
#     return -1

# phase_permutations = list(permutations([5,6,7,8,9]))

# max_power = 0
# for phases in phase_permutations:
#   amps = [
#     Amplifier(intcode[:], phases[0], True),
#     Amplifier(intcode[:], phases[1]),
#     Amplifier(intcode[:], phases[2]),
#     Amplifier(intcode[:], phases[3]),
#     Amplifier(intcode[:], phases[4])
#   ]
#   amp_index = 0
#   count = 0
#   while True:
#     # print(amp_index)
#     current_amp = amps[amp_index]
#     # print('Running amp {0} with input {1} at inst pointer {2}'.format(amp_index, current_amp.inputs, current_amp.instruction_pointer))
#     run_status_code = current_amp.run()
#     # print('Output: {0}'.format(current_amp.output))
#     if run_status_code != -1:
#       next_amp_index = amp_index + 1 if amp_index < len(amps) - 1 else 0
#       amps[next_amp_index].inputs.append(current_amp.output)
#       amp_index = next_amp_index
#     else:
#       power = amps[4].output
#       if power > max_power:
#         max_power = power
#       break
#     count += 1

# print(max_power)

phases = [9, 8, 7, 6, 5]

intcode_computers = [
  IntcodeComputer(intcode[:], [phases[0], 0]),
  IntcodeComputer(intcode[:], [phases[1]]),
  IntcodeComputer(intcode[:], [phases[2]]),
  IntcodeComputer(intcode[:], [phases[3]]),
  IntcodeComputer(intcode[:], [phases[4]])
]

any_computers_halted = True in map(lambda ic: ic.halted, intcode_computers)

computer_index = 0
while not any_computers_halted:
  computer = intcode_computers[computer_index]
  current_output = computer.output
  while computer.output == current_output and computer.halted == False:
    computer.perform_next_operation()
  next_computer_index = 0 if computer_index == len(intcode_computers)-1 else computer_index + 1
  intcode_computers[next_computer_index].inputs.append(computer.output)

print(intcode_computers[4].output)

