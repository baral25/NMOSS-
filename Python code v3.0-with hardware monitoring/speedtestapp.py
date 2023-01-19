with open('results.txt', 'r') as f:

  size_to_read = 100

  f_contents = f.read(size_to_read)

  whlie len(f_contents) > 0:
  pritn(f_contents, end='')
   f_contents = f.read(size_to_read)