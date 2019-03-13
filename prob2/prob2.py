##!/usr/local/bin/python3
# -------------------------------
# APC 523, Pset #1, Problem 2
# Cristian Lacey
# -------------------------------
import math

# -------------------------------
# PART a)
# -------------------------------
def round_to_n(x,r):
    '''Rounds x to r significant digits.'''
    return float('%.*g' % (r,x))

def fact(x,r):
    '''Returns factorial of x, rounding to r significant digits after each
    operation.'''
    f = round_to_n(1,r)
    for i in range(2,x+1):
        f = f*round_to_n(i,r)
    return f

def exp_sum(x,n,r,dir='right',print_e=False):
    '''Finds the nth order partial sum for exp(x) evaluated at x, rounding to r
    significant figures at each step in the calculation. Keywarg 'dir'
    determines how the final term series is summed. dir = 'right' sums left to
    right, and vice versa. If x < 0, then certain terms in the partial sum
    will be negative. The dir = 'neg_left' and dir = 'neg_right' options
    will perform the sum for the negative and positive terms separately,
    preserving the term order, with the sum taken in the indicated direction.'''
    x = round_to_n(x,r)

    # Build term list of partial sum, e
    e = [1,x]
    for i in range(2,n+1):
        x_n = x
        for j in range(i-1):
            x_n = round_to_n(x_n*x,r)
        e_n = x_n/round_to_n(fact(i,r),r)
        e_n = round_to_n(e_n,r)
        e.append(e_n)
    if print_e:
        print('{:>14} {:>18}'.format('Value of n','Calculated t_n'))
        for (i,x) in enumerate(e):
            print('{:>14} {:>18.4e}'.format(i, x))

    # Sum e based on user-specified algorithm
    e_tot = 0
    if dir == 'right':
        for i in e:
            e_tot += i
            e_tot = round_to_n(e_tot,r)
    elif dir == 'left':
        for i in e[::-1]:
            e_tot += i
            e_tot = round_to_n(e_tot,r)
    elif dir == 'neg_right':
        e_neg = [x for x in e if x < 0]
        e_pos = [x for x in e if x > 0]
        e_subneg = 0
        e_subpos = 0
        for i in e_neg:
            e_subneg += i
            e_subneg = round_to_n(e_subneg,r)
        for i in e_pos:
            e_subpos += i
            e_subpos = round_to_n(e_subpos,r)
        e_tot = e_subneg + e_subpos
        e_tot = round_to_n(e_tot,r)
    elif dir == 'neg_left':
        e_neg = [x for x in e if x < 0]
        e_pos = [x for x in e if x > 0]
        e_subneg = 0
        e_subpos = 0
        for i in e_neg[::-1]:
            e_subneg += i
            e_subneg = round_to_n(e_subneg,r)
        for i in e_pos[::-1]:
            e_subpos += i
            e_subpos = round_to_n(e_subpos,r)
        e_tot = e_subneg + e_subpos
        e_tot = round_to_n(e_tot,r)

    return e_tot

# 244.691932264 <--- from a calculator
print('-'*50+'\n'+'PART a)\n'+'-'*50)
S_30r = exp_sum(5.5,30,5,dir='right',print_e=True)
S_30l = exp_sum(5.5,30,5,dir='left')
print('\nexp(5.5) calculated adding left to right, with 30 terms: %.2f' % S_30r)
print('exp(5.5) calculated adding right to left, with 30 terms: %.2f' % S_30l)

# -------------------------------
# PART b)
# -------------------------------
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART b)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(5.5,i,5,dir='right')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(5.5),5)

rel_err = (a-e_calc)/e_calc
print('\nexp(5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# -------------------------------
# PART c)
# -------------------------------
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART c)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(5.5,i,5,dir='left')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(5.5),5)

rel_err = (a-e_calc)/e_calc
print('\nexp(5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# -------------------------------
# PART d)
# -------------------------------
# PART i) add left to right
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART d) i)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(-5.5,i,5,dir='right')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(-5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(-5.5),5)

rel_err = abs(a-e_calc)/e_calc
print('\nexp(-5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# PART ii) add right to left
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART d) ii)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(-5.5,i,5,dir='left')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(-5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(-5.5),5)

rel_err = abs(a-e_calc)/e_calc
print('\nexp(-5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# PART iii) add neg and positive separately, both left to right
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART d) iii)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(-5.5,i,5,dir='neg_right')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(-5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(-5.5),5)

rel_err = abs(a-e_calc)/e_calc
print('\nexp(-5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# PART iv) add neg and positive separately, both right to left
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART d) iv)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = exp_sum(-5.5,i,5,dir='neg_left')
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(-5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(-5.5),5)

rel_err = abs(a-e_calc)/e_calc
print('\nexp(-5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)

# -------------------------------
# PART e)
# -------------------------------
i = 1
a_prev = 0.1
a = 1

print('-'*50+'\n'+'PART e)\n'+'-'*50)
print('{:>14} {:>18}'.format('Value of k','Calculated S_k'))
print('{:>14} {:>18.5g}'.format(0, 1))
while (abs(round_to_n(a,5)-round_to_n(a_prev,5)) > 0):
    a_prev = a
    a = round_to_n(float(1),5)/exp_sum(5.5,i,5,dir='left')
    a = round_to_n(a,5)
    i += 1
    print('{:>14} {:>18.5g}'.format((i-1), a))

print('\n5 significant figure convergence with k = %d' % (i-1))
print('k = %d, exp(-5.5) = %#.5g' % ((i-1),a))

e_calc = round_to_n(math.exp(-5.5),5)

rel_err = abs(a-e_calc)/e_calc
print('\nexp(-5.5) calculated with math.exp() = %#.5g' % e_calc)
print('Relative error = %.5e' % rel_err)
