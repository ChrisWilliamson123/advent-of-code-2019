from collections import defaultdict

class IntcodeComputer:
  def __init__(self, intcode, inputs):
    self.intcode = intcode
    self.inputs = inputs
    self.ip = 0
    self.output = 0
    self.halted = False
    self.memory = defaultdict(int)
    for i in range(len(intcode)):
      self.memory[i] = intcode[i]

  # Takes in an operation spec such as 1002
  # Returns [opcode, param1_mode, param2_mode, param3_mode]
  # E.g. 1002 -> (2, [0, 1, 0])
  def parse_operation_spec(self, spec):
    as_string = str(spec)
    opcode = int(as_string[-2:])
    param_modes = map(lambda x: int(x), list(as_string[0:-2])[::-1])
    while len(param_modes) < 2:
      param_modes.append(0)

    return (opcode, param_modes)

  # Returns: list [value1, value2]
  # Will only return two values if operation needs both
  def get_param_values(self, opcode, param1_mode, param2_mode):
    if opcode == 3:
      return []

    value1 = self.memory[self.ip+1] if param1_mode else self.memory[self.memory[self.ip+1]]

    if opcode == 4:
      return [value1]
    else:
      value2 = self.memory[self.ip+2] if param2_mode else self.memory[self.memory[self.ip+2]]
      return [value1, value2]

  def skip_ahead_amount(self, opcode):
    return {
      1: 4,
      2: 4,
      3: 2,
      4: 2,
      5: 0,
      6: 0,
      7: 4,
      8: 4,
      9: 2
    }[opcode]

  def op_add(self, value1, value2, destination_address):
    self.memory[destination_address] = value1 + value2

  def op_mul(self, value1, value2, destination_address):
    self.memory[destination_address] = value1 * value2

  def op_input(self, destination_address):
    self.memory[destination_address] = self.inputs.pop(0)

  def op_jit(self, value1, value2):
    self.ip = value2 if value1 != 0 else self.ip + 3

  def op_jif(self, value1, value2):
    self.ip = value2 if value1 == 0 else self.ip + 3

  def op_lt(self, value1, value2, destination_address):
    self.memory[destination_address] = 1 if value1 < value2 else 0

  def op_eq(self, value1, value2, destination_address):
    self.memory[destination_address] = 1 if value1 == value2 else 0

  def perform_next_operation(self):
    # Get the operation specification
    (opcode, [param1_mode, param2_mode]) = self.parse_operation_spec(self.memory[self.ip])
    if opcode == 99:
      self.halted = True
      return
      
    values = self.get_param_values(opcode, param1_mode, param2_mode)

    if opcode == 1:
      self.op_add(values[0], values[1], self.memory[self.ip+3])
    elif opcode == 2:
      self.op_mul(values[0], values[1], self.memory[self.ip+3])
    elif opcode == 3:
      self.op_input(self.memory[self.ip+1])
    elif opcode == 4:
      # self.op_output(values[0])
      self.output = values[0]
    elif opcode == 5:
      self.op_jit(values[0], values[1])
    elif opcode == 6:
      self.op_jif(values[0], values[1])
    elif opcode == 7:
      self.op_lt(values[0], values[1], self.memory[self.ip+3])
    elif opcode == 8:
      self.op_eq(values[0], values[1], self.memory[self.ip+3])

    self.ip += self.skip_ahead_amount(opcode)

  def run_program(self):
    while not self.halted:
      self.perform_next_operation()
