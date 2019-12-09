from itertools import permutations

def skip_ahead_amount(opcode):
  return {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 0,
    6: 0,
    7: 4,
    8: 4
  }[opcode]

# Takes in an operation spec such as 1002
# Returns [opcode, param1_mode, param2_mode, param3_mode]
# E.g. 1002 -> (2, [0, 1, 0])
def parse_operation_spec(spec):
  as_string = str(spec)
  opcode = int(as_string[-2:])
  param_modes = map(lambda x: int(x), list(as_string[0:-2])[::-1])
  while len(param_modes) < 3:
    param_modes.append(0)

  return (opcode, param_modes)

def get_param_values(intcode, instruction_pointer, param1_mode, param2_mode):
  value1 = intcode[instruction_pointer+1] if param1_mode else intcode[intcode[instruction_pointer+1]]
  value2 = intcode[instruction_pointer+2] if param2_mode else intcode[intcode[instruction_pointer+2]]
  return (value1, value2)

def op_input(intcode, input_value, dest):
  intcode[dest] = input_value

def op_add(intcode, value1, value2, dest):
  intcode[dest] = value1 + value2

def op_mul(intcode, value1, value2, dest):
  intcode[dest] = value1 * value2

def run_program(intcode, inputs):
  instruction_pointer = 0
  output = 0

  # Get the first operation and it's parameter modes
  operation_spec = parse_operation_spec(intcode[instruction_pointer])
  while operation_spec[0] != 99:
    opcode = operation_spec[0]
    parameter_modes = operation_spec[1]
    param1_mode = parameter_modes[0]
    param2_mode = parameter_modes[1]

    # Addition
    if opcode == 1:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      destination_address = intcode[instruction_pointer+3]
      op_add(intcode, value1, value2, destination_address)
    # Multiplication
    elif opcode == 2:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      destination_address = intcode[instruction_pointer+3]
      op_mul(intcode, value1, value2, destination_address)
    # Input
    elif opcode == 3:
      op_input(intcode, inputs[0], intcode[instruction_pointer+1])
      inputs.pop(0)
    # Output
    elif opcode == 4:
      if param1_mode == 1:
        output = intcode[instruction_pointer+1]
      else:
        output = intcode[intcode[instruction_pointer+1]]
    # Jump-if-true
    elif opcode == 5:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      if value1 != 0:
        instruction_pointer = value2
      else:
        instruction_pointer += 3
    # Jump-if-false
    elif opcode == 6:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      if value1 == 0:
        instruction_pointer = value2
      else:
        instruction_pointer += 3
    # Less than
    elif opcode == 7:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      to_store = 0
      if value1 < value2:
        to_store = 1
      intcode[intcode[instruction_pointer+3]] = to_store
    # Equals
    elif opcode == 8:
      (value1, value2) = get_param_values(intcode, instruction_pointer, param1_mode, param2_mode)
      to_store = 0
      if value1 == value2:
        to_store = 1
      intcode[intcode[instruction_pointer+3]] = to_store

    instruction_pointer += skip_ahead_amount(opcode)
    operation_spec = parse_operation_spec(intcode[instruction_pointer])

  return output

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

max_power_output = 0
for phases in permutations([0, 1, 2, 3, 4]):
  latest_amp_output = 0
  for i in range(5):
    latest_amp_output = run_program(intcode[:], [phases[i], latest_amp_output])
  if latest_amp_output > max_power_output:
    max_power_output = latest_amp_output

print(max_power_output)

class Amplifier:
  def __init__(self, intcode, phase, first = False):
    self.intcode = intcode
    self.phase = phase
    self.instruction_pointer = 0
    self.inputs = [phase]
    if first:
      self.inputs.append(0)
    self.output = 0

  def run(self):
    operation_spec = parse_operation_spec(self.intcode[self.instruction_pointer])
    while operation_spec[0] != 99:
      opcode = operation_spec[0]
      parameter_modes = operation_spec[1]
      param1_mode = parameter_modes[0]
      param2_mode = parameter_modes[1]

      # Addition
      if opcode == 1:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        destination_address = self.intcode[self.instruction_pointer+3]
        op_add(self.intcode, value1, value2, destination_address)
      # Multiplication
      elif opcode == 2:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        destination_address = self.intcode[self.instruction_pointer+3]
        op_mul(self.intcode, value1, value2, destination_address)
      # Input
      elif opcode == 3:
        op_input(self.intcode, self.inputs[0], self.intcode[self.instruction_pointer+1])
        self.inputs.pop(0)
      # Output
      elif opcode == 4:
        if param1_mode == 1:
          self.output = self.intcode[self.instruction_pointer+1]
        else:
          self.output = self.intcode[self.intcode[self.instruction_pointer+1]]
        self.instruction_pointer += skip_ahead_amount(opcode)
        return 0
      # Jump-if-true
      elif opcode == 5:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        if value1 != 0:
          self.instruction_pointer = value2
        else:
          self.instruction_pointer += 3
      # Jump-if-false
      elif opcode == 6:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        if value1 == 0:
          self.instruction_pointer = value2
        else:
          self.instruction_pointer += 3
      # Less than
      elif opcode == 7:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        to_store = 0
        if value1 < value2:
          to_store = 1
        self.intcode[self.intcode[self.instruction_pointer+3]] = to_store
      # Equals
      elif opcode == 8:
        (value1, value2) = get_param_values(self.intcode, self.instruction_pointer, param1_mode, param2_mode)
        to_store = 0
        if value1 == value2:
          to_store = 1
        self.intcode[self.intcode[self.instruction_pointer+3]] = to_store

      self.instruction_pointer += skip_ahead_amount(opcode)
      operation_spec = parse_operation_spec(self.intcode[self.instruction_pointer])
    return -1

max_power = 0
for phases in permutations([5,6,7,8,9]):
  amps = [
    Amplifier(intcode[:], phases[0], True),
    Amplifier(intcode[:], phases[1]),
    Amplifier(intcode[:], phases[2]),
    Amplifier(intcode[:], phases[3]),
    Amplifier(intcode[:], phases[4])
  ]
  amp_index = 0
  count = 0
  while True:
    current_amp = amps[amp_index]
    run_status_code = current_amp.run()
    if run_status_code != -1:
      next_amp_index = amp_index + 1 if amp_index < len(amps) - 1 else 0
      amps[next_amp_index].inputs.append(current_amp.output)
      amp_index = next_amp_index
    else:
      power = amps[4].output
      if power > max_power:
        max_power = power
      break
    count += 1

print(max_power)




