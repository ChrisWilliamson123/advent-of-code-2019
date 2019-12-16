from itertools import islice, chain, cycle

input = [int(x) for x in open('input.txt', 'r').read()]
# input = [int(x) for x in open('test_input.txt', 'r').read()]

# print(input)

repeating_pattern_base = [0, 1, 0, -1]
# current_pattern = (input[:])
current_pattern = (input[:] * 10000)

phases = 100
offset = 5970221

current_pattern_length = len(current_pattern)
half_pattern_length = current_pattern_length / 2

for i in range(phases):
  total = 0
  output = []
  for j in range(current_pattern_length, offset, -1):
    total += current_pattern[j-1]
    total %= 10
    output.append(total)
  current_pattern = current_pattern[0:offset] + output[::-1]

print(''.join([str(x) for x in current_pattern[offset:offset+8]]))