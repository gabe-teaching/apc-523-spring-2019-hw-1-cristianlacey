#!/usr/local/bin/python3
# -------------------------------
# APC 523, Pset #1, Problem 5
# Cristian Lacey
# -------------------------------

i = 0
a_prev = 0
a = 1

print('Loop Iteration       Value of n       Calculated e')
while (abs(a-a_prev) > float(1e-13)):
    a_prev = a
    n = 10**i
    a = ((n+1)/n)**(n)
    i += 1
    print('{:>14} {:>16.0e} {:>18.13f}'.format(i, n, a))

print('\n12 significant figure convergence after %d iterations' % i)
print('n_stop = %.1e, e_final = %.11f' % (n,a))
