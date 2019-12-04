intcode = [int(x) for x in open('input.txt', 'r').read().split(',')]

def insert_inputs(intcode, noun, verb):
  intcode[1] = noun 
  intcode[2] = verb
  return intcode

def add(intcode, pos1, pos2, resPos):
    intcode[resPos]=intcode[pos1]+intcode[pos2]
    
def mul(intcode, pos1, pos2, resPos):
    intcode[resPos]=intcode[pos1]*intcode[pos2]

def run_intcode(intcode, noun, verb):
  intcode = insert_inputs(intcode, noun, verb)

  index = 0
  operation = intcode[index]

  while operation != 99:
    if operation == 1:
        add(intcode, intcode[index+1], intcode[index+2], intcode[index+3])
    elif operation == 2:
        mul(intcode, intcode[index+1], intcode[index+2], intcode[index+3])
        
    index+=4
    operation=intcode[index] 

  return intcode[0]

part_one_input = intcode[:]
part_one = run_intcode(part_one_input, 12, 2)
print(part_one)

for noun in range(100):
  for verb in range(100):
    ic = intcode[:]
    output = run_intcode(ic, noun, verb)

    if output == 19690720:
      print(100 * noun + verb)
      exit(0)