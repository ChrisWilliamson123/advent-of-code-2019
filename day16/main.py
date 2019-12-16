input = [int(x) for x in open('input.txt', 'r').read()]

current_pattern = (input * 10000)

phases = 100
offset = int(''.join(map(str,input[0:7])))

pattern_length = len(current_pattern)

for i in range(phases):
  total = 0
  output = []
  for j in range(pattern_length, offset, -1):
    total = (total + current_pattern[j-1]) % 10
    output.append(total)
  current_pattern = current_pattern[:offset] + output[::-1]

print(''.join([str(x) for x in current_pattern[offset:offset+8]]))
