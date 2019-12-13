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

  def perform_next_operation(self):
    (opcode, modes) = self.parse_operation_spec(self.memory[self.ip])
    
    if opcode == 99:
      self.halted = True
      return

    addresses = self.get_addresses_from_parameter_modes(modes)

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
      self.op_change_relative_base(addresses[0])

    self.ip += self.skip_ahead_amount(opcode)

  def parse_operation_spec(self, spec):
    opcode = int(str(spec)[-2:]) 
    param_modes =  [(spec//100)%10, (spec//1000)%10, (spec//10000)%10]
    return (opcode, param_modes)

  def get_addresses_from_parameter_modes(self, modes):
    addresses = []
    for i in range(len(modes)):
      parameter_location = self.ip + i + 1
      # RELATIVE
      if modes[i] == 2:
        addresses.append(self.relative_base + self.memory[parameter_location])
      # IMMEDIATE
      elif modes[i] == 1:
        addresses.append(parameter_location)
      # POSTION
      else:
        addresses.append(self.memory[parameter_location])
    return addresses

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

  def op_change_relative_base(self, addr1):
    self.relative_base += self.memory[addr1]

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
