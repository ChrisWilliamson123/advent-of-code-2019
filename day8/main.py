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
