##!/usr/local/bin/python3
# -------------------------------
# APC 523, Pset #1, Problem 7
# Cristian Lacey
# -------------------------------
import numpy as np
from matplotlib import pyplot as plt
import sympy as sym
# from scipy.optimize import newton
import scipy.optimize as opt
import numpy.polynomial.polynomial as polynomial

# NOTE: If you get an error, try running the code from a virtual environment
# through Anaconda. For some reason, the opt.newton() function doesn't play
# nice with symbolic polynomials when using pip installed versions of numpy
# and sympy. Just in case, here's the output:
'''
----------------------------------------
PART a)
----------------------------------------
20th order Wilkinson poly is: Poly(x**20 - 210*x**19 + 20615*x**18 -
1256850*x**17 + 53327946*x**16 - 1672280820*x**15 + 40171771630*x**14 -
756111184500*x**13 + 11310276995381*x**12 - 135585182899530*x**11 +
1307535010540395*x**10 - 10142299865511450*x**9 + 63030812099294896*x**8 -
311333643161390640*x**7 + 1206647803780373360*x**6 - 3599979517947607200*x**5 +
8037811822645051776*x**4 - 12870931245150988800*x**3 +
3803759753640704000*x**2 - 8752948036761600000*x + 2432902008176640000,
x, domain='ZZ')
----------------------------------------
PART b)
----------------------------------------
Newton-Raphson: 19.9999949571418
Built-in Poly method: 19.999809291236637
----------------------------------------
PART c)
----------------------------------------
Coefficient, a_20      Newton Root (initial guess 21)               Poly1D Root
       1.00000001                            9.585390       20.647583+1.186926j
       1.00000100                            7.752713       23.149016+2.740985j
       1.00010000                            5.969335       28.400212+6.510434j
       1.01000000                            5.469593      38.478184+20.834324j
----------------------------------------
PART d)
----------------------------------------
Coefficient, a_19                Root 16                Root 17
-210.000000119209    16.730745-2.812625j    16.730745+2.812625j
----------------------------------------
PART e)
----------------------------------------
                k          Root, Omega_k           cond Omega_k
                0               1.000000               4.200e+2
                1               2.000000               4.389e+4
                2               3.000000               2.019e+6
                3               4.000000               5.148e+7
                4               5.000001               8.237e+8
                5               5.999989               8.923e+9
                6               7.000102              6.886e+10
                7               7.999356              3.910e+11
                8               9.002915              1.690e+12
                9               9.990413              5.492e+12
               10              11.025023              1.451e+13
               11              11.953283              2.857e+13
               12              13.074314              4.494e+13
               13              13.914756              5.943e+13
               14              15.075494              4.728e+13
               15              15.946287              3.936e+13
               16              17.025427              1.712e+13
               17              17.990921              6.572e+12
               18              19.001910              1.367e+12
               19              19.999809              1.380e+11
[Finished in 1.561s]
'''
# -------------------------------
# PART a)
# -------------------------------
def wilkinson(x,n):
    '''Returns symbolic nth order Wilkinson polynomial'''
    y = (x-1)
    for i in range(2,n+1):
        y = y*(x-i)
    poly = sym.Poly(sym.expand(y))

    return poly

x = sym.Symbol('x')
poly = wilkinson(x,20)
coeffs = poly.coeffs()

print('-'*40+'\n'+'PART a)\n'+'-'*40)
print('20th order Wilkinson poly is: ' + str(poly))

# -------------------------------
# PART b)
# -------------------------------
def find_roots(poly,init):
    roots = opt.newton(poly,init,maxiter=10000,tol=float(1e-8))

    return roots

y = polynomial.Polynomial(coeffs[::-1])
root = find_roots(y,21)

root_alt = np.poly1d(coeffs).r[0]

print('-'*40+'\n'+'PART b)\n'+'-'*40)
print('Newton-Raphson: '+str(root))
print('Built-in Poly method: '+str(root_alt))

# -------------------------------
# PART c)
# -------------------------------
print('-'*40+'\n'+'PART c)\n'+'-'*40)
print('{:>17} {:>35} {:>25}'.format('Coefficient, a_20',  'Newton Root (initial guess 21)', 'Poly1D Root'))

delta = [float(1e-8),float(1e-6),float(1e-4),float(1e-2)]
og_coeffs = coeffs
for d in delta:
    coeffs = og_coeffs.copy()
    coeffs[0] += d

    y = polynomial.Polynomial(coeffs[::-1])
    root = find_roots(y,21)

    root_alt = np.poly1d(coeffs).r[0]

    print('{:>17.8f} {:>35.6f} {:>25.6f}'.format(coeffs[0], root, root_alt))

# -------------------------------
# PART d)
# -------------------------------
coeffs = og_coeffs.copy()
coeffs[1] += (-2**(-23))

y = polynomial.Polynomial(coeffs[::-1])

# roots = []
# for i in range(0,25):
#     for j in range(10):
#         root = find_roots(y,i+j/10)
#         root = round(root,3)
#         if root not in roots:
#             roots.append(root)
# roots = sorted(roots)
# print(roots,len(roots))

# root16 = roots[15]
# root17 = roots[16]

root16 = np.poly1d(coeffs).r[4]
root17 = np.poly1d(coeffs).r[3]

# root16 = find_roots(y,16)
# root17 = find_roots(y,17)

print('-'*40+'\n'+'PART d)\n'+'-'*40)
print('{:>17} {:>22} {:>22}'.format('Coefficient, a_19',  'Root 16', 'Root 17'))
print('{:>17} {:>22.6f} {:>22.6f}'.format(str(coeffs[1]), root16, root17))

# roots2 = 0#poly.roots()
# print(roots1,roots2)

# polytest = np.polynomial.polynomial.Polynomial(np.array([-4,0,1]))
# roottest = opt.newton(polytest.__call__,3)
# print(roottest)

# -------------------------------
# PART e)
# -------------------------------
coeffs = og_coeffs.copy()
poly = np.poly1d(coeffs)
poly_deriv = np.poly1d.deriv(poly)
roots = poly.r[::-1]

# print(roots)

coeffs = coeffs[::-1]
cond = []
for k in range(len(coeffs)-1):
    sum = 0
    for l in range(len(coeffs)-1):
        sum += abs((coeffs[l]*roots[k]**(l-1))/poly_deriv(roots[k]))
    cond.append(sum)

print('-'*40+'\n'+'PART e)\n'+'-'*40)
print('{:>17} {:>22} {:>22}'.format('k',  'Root, Omega_k', 'cond Omega_k'))
for i in range(len(coeffs)-1):
    print('{:>17} {:>22.6f} {:>22.3e}'.format(str(i), roots[i], cond[i]))
