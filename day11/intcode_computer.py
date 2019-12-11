from collections import defaultdict

class IntcodeComputer:
  def __init__(self, intcode, inputs):
    self.intcode = intcode
    self.inputs = inputs
    self.ip = 0
    self.outputs = []
    self.relative_base = 0
    self.halted = False
    self.memory = defaultdict(int)
    for i in range(len(intcode)):
      self.memory[i] = intcode[i]

    self.painted_white_panels = set()
    self.painted_black_panels = set()
    self.output_mode = 0
    self.position = (0,0)
    self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    self.direction = 0
    self.painted_tiles = {}


  # Takes in an operation spec such as 1002
  # Returns [opcode, param1_mode, param2_mode, param3_mode]
  # E.g. 1002 -> (2, [0, 1, 0])
  def parse_operation_spec(self, spec):
    as_string = str(spec)
    opcode = int(as_string[-2:])
    param_modes = map(lambda x: int(x), list(as_string[0:-2])[::-1])
    while len(param_modes) < 3:
      param_modes.append(0)

    return (opcode, param_modes)

  # Returns: list [value1, value2]
  # Will only return two values if operation needs both
  def get_param_values(self, opcode, modes):
    values = []
    for i in range(1, len(modes)+1):
      if modes[i-1] == 2:
        # print('XX: {0}')
        values.append(self.memory[self.relative_base + self.memory[self.ip+i]])
      elif modes[i-1] == 1:
        values.append(self.memory[self.ip+i])
      else:
        values.append(self.memory[self.memory[self.ip+i]])
    return values

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

  def get_dest_addr(self, mode, value):
    if mode == 2:
      return self.relative_base + value
    return value

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
    (opcode, [param1_mode, param2_mode, param3_mode]) = self.parse_operation_spec(self.memory[self.ip])
    
    if opcode == 99:
      self.halted = True
      return
      
    values = self.get_param_values(opcode, [param1_mode, param2_mode, param3_mode])

    if opcode == 1:
      self.op_add(values[0], values[1], self.get_dest_addr(param3_mode, self.memory[self.ip+3]))
    elif opcode == 2:
      self.op_mul(values[0], values[1], self.get_dest_addr(param3_mode, self.memory[self.ip+3]))
    elif opcode == 3:
      print('Input instruction')
      if param1_mode == 2:
        input_address = self.memory[self.ip+1] + self.relative_base
      else:
        input_address = self.memory[self.ip+1]
      if self.position in self.painted_tiles:
        self.memory[input_address] = self.painted_tiles[self.position]
      else:
        self.memory[input_address] = 1 if len(self.painted_tiles) == 0 else 0
    elif opcode == 4:
      print('Outputting {0}'.format(values[0]))
      output_value = values[0]
      self.outputs.append(output_value)
      if self.output_mode == 0:
        if output_value == 0:
          self.painted_tiles[self.position] = 0
        else:
          self.painted_tiles[self.position] = 1
        self.output_mode = 1
        print('Painted {0} {1}'.format(self.position, output_value))
      else:
        if output_value == 0:
          self.direction = len(self.directions) - 1 if self.direction == 0 else self.direction - 1
        else:
          self.direction = 0 if self.direction == len(self.directions) - 1 else self.direction + 1
        self.position = (self.position[0] + self.directions[self.direction][0], self.position[1] + self.directions[self.direction][1])
        print('New pos: {0}'.format(self.position))
        self.output_mode = 0
    elif opcode == 5:
      self.op_jit(values[0], values[1])
    elif opcode == 6:
      self.op_jif(values[0], values[1])
    elif opcode == 7:
      self.op_lt(values[0], values[1], self.get_dest_addr(param3_mode, self.memory[self.ip+3]))
    elif opcode == 8:
      self.op_eq(values[0], values[1], self.get_dest_addr(param3_mode, self.memory[self.ip+3]))
    elif opcode == 9:
      param = self.memory[self.ip+1]
      if param1_mode == 2:
        change = self.memory[self.relative_base + param]
      elif param1_mode == 1:
        change = param
      else:
        change = self.memory[param]
      self.relative_base += change

    self.ip += self.skip_ahead_amount(opcode)

  def run_program(self):
    while not self.halted:
      self.perform_next_operation()
