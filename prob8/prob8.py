##!/usr/local/bin/python3
# -------------------------------
# APC 523, Pset #1, Problem 8
# Cristian Lacey
# -------------------------------
import math
e = math.exp(1)
# Part d)
N = 32
k = 20
y_n = 0

print('-'*40+'\n'+'PART d)\n'+'-'*40)
print('{:>17} {:>35} {:>25}'.format('n',  'y_n', 'y_(n-1)'))
for n in range(N,k,-1):
    y_nn = (e - y_n)/n
    print('{:>17} {:>35.6f} {:>25.9f}'.format(n, y_n, y_nn))
    y_n = y_nn

print('\nFinal calculated value for y_20 = %.6f' % y_n)
