
import numpy

s = raw_input()

s = s.split(' ')

s = map(float, s)

a = numpy.array(s)

ra = a [::-1]

print ra
