def skip_ahead_amount(opcode):
  if opcode in [1, 2, 7, 8]:
    return 4
  elif opcode in [5, 6]:
    return 0
  else:
    return 2

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

intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

input_id = 5
instruction_pointer = 0
latest_output = 0

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
    op_input(intcode, input_id, intcode[instruction_pointer+1])
  # Output
  elif opcode == 4:
    if param1_mode == 1:
      latest_output = intcode[instruction_pointer+1]
    else:
      latest_output = intcode[intcode[instruction_pointer+1]]
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

print(latest_output)