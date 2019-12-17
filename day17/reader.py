for l in open('functions.txt', 'r').readlines():
  to_print = ''
  for c in l.strip():
    to_print += str(ord(c)) + ','
  print(to_print)