from collections import Counter

image_digits = list(open('input.txt', 'r').read())
image_width = 25
image_depth = 6
layer_size = image_width * image_depth

layers = [image_digits[x:x+layer_size] for x in range(0, len(image_digits), layer_size)]
counted_layers = map(lambda l: Counter(l), layers)
layer_with_min_zeros = min(counted_layers, key=lambda counts: counts['0'])
part_one = layer_with_min_zeros['1'] * layer_with_min_zeros['2']
print(part_one)

def get_visible_pixel(position, layers):
  for layer in layers:
    if layer[position] != '2':
      return layer[position]

final_image = map(lambda pos: get_visible_pixel(pos, layers), range(layer_size))
final_image_in_rows = [final_image[x:x+image_width] for x in range(0, len(final_image), image_width)]

def print_image(image):
  for row in image:
    print(''.join(map(lambda p: ' ' if p == '0' else '#', row)))

print_image(final_image_in_rows)


