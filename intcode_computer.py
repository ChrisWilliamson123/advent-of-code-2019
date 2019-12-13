from collections import defaultdict
from itertools import cycle

class IntcodeComputer:
  def __init__(self, intcode, inputs):
    self.memory = defaultdict(int)
    for i in range(len(intcode)):
      self.memory[i] = intcode[i]

    self.inputs = inputs
    self.outputs = []

    self.ip = 0
    self.relative_base = 0
    
    self.halted = False

  def parse_operation_spec(self, spec):
    opcode = int(str(spec)[-2:]) 
    param_modes =  [(spec//100)%10, (spec//1000)%10, (spec//10000)%10]
    return (opcode, param_modes)

  def get_addresses_from_parameter_modes(self, modes):
    addresses = []
    for i in range(1, len(modes)+1):
      parameter_location = self.ip + i
      # RELATIVE
      if modes[i-1] == 2:
        addresses.append(self.relative_base + self.memory[parameter_location])
      # IMMEDIATE
      elif modes[i-1] == 1:
        addresses.append(parameter_location)
      # POSTION
      else:
        addresses.append(self.memory[parameter_location])
    return addresses

  # Returns: list [value1, value2]
  # Will only return two values if operation needs both
  def get_param_values(self, opcode, modes):
    values = []
    for i in range(1, len(modes)+1):
      if modes[i-1] == 2:
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

  def get_result_addr(self, mode, value):
    if mode == 2:
      return self.relative_base + value
    return value

  def op_add(self, addr1, addr2, result_addr):
    self.memory[result_addr] = self.memory[addr1] + self.memory[addr2]

  def op_mul(self, addr1, addr2, result_addr):
    self.memory[result_addr] = self.memory[addr1] * self.memory[addr2]

  def op_input(self, result_addr):
    self.memory[result_addr] = self.inputs.pop()

  def op_output(self, addr1):
    self.outputs.append(self.memory[addr1])

  def op_jit(self, addr1, addr2):
    self.ip = self.memory[addr2] if self.memory[addr1] != 0 else self.ip + 3

  def op_jif(self, addr1, addr2):
    self.ip = self.memory[addr2] if self.memory[addr1] == 0 else self.ip + 3

  def op_lt(self, addr1, addr2, result_addr):
    self.memory[result_addr] = 1 if self.memory[addr1] < self.memory[addr2] else 0

  def op_eq(self, addr1, addr2, result_addr):
    self.memory[result_addr] = 1 if self.memory[addr1] == self.memory[addr2] else 0

  def perform_next_operation(self):
    # Get the operation specification
    (opcode, [param1_mode, param2_mode, param3_mode]) = self.parse_operation_spec(self.memory[self.ip])
    
    if opcode == 99:
      self.halted = True
      return
      
    values = self.get_param_values(opcode, [param1_mode, param2_mode, param3_mode])
    addresses = self.get_addresses_from_parameter_modes([param1_mode, param2_mode, param3_mode])

    if opcode == 1:
      self.op_add(addresses[0], addresses[1], addresses[2])
    elif opcode == 2:
      self.op_mul(addresses[0], addresses[1], addresses[2])
    elif opcode == 3:
      self.op_input(addresses[0])
    elif opcode == 4:
      self.op_output(addresses[0])
    elif opcode == 5:
      self.op_jit(addresses[0], addresses[1])
    elif opcode == 6:
      self.op_jif(addresses[0], addresses[1])
    elif opcode == 7:
      self.op_lt(addresses[0], addresses[1], addresses[2])
    elif opcode == 8:
      self.op_eq(addresses[0], addresses[1], addresses[2])
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
