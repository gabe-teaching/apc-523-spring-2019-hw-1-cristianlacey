#!/usr/local/bin/python3
# -------------------------------
# APC 523, Pset #1, Problem 6
# Cristian Lacey
# -------------------------------
import numpy as np
from matplotlib import pyplot as plt

def root_square(x,iter,plt_mode=False):
    ''' Takes a numpy array, takes the square root of each element an "iter"
    number of times. It then attempts to return the resulting array to the
    original input by taking the square of the result an "iter" number of times.
    Returns the absolute value of the maximum difference between the overall
    resulting array and the original array.'''
    y = x
    yi = x

    for i in range(iter):
        yi = np.sqrt(yi)

    yf = yi

    for i in range(iter):
        yf = np.square(yf)

    # Jank method of grabbing closest points to y = x line
    dx = np.diff(yf)
    inds = np.array((dx>0.0001).nonzero())
    inds = inds+1
    inds = np.append([0],inds)

    err = np.abs(y-yf)
    err_max = np.amax(err)

    if plt_mode:
        plt.figure()
        plt.title("iter = %d" % iter)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x,y,'k--',label='y = x')
        # plt.plot(x,yi,'b',label=r'yi = $x^{\frac{1}{2^{iter}}}$')
        plt.plot(x,yf,'k',label=r'$y_{f}$ = ${(x^{\frac{1}{2^{iter}}})}^{2^{iter}}$')
        plt.plot(x[inds],yf[inds],'r.')
        plt.legend(loc='lower right')
        plt.show()

    return err_max, x, y, yi, yf, inds

# -------------------------------
# Main (Generates all analysis)
# -------------------------------
x = np.linspace(1.0, 10.0, num=1001)

# Initial run with 52 iterations (number of times to take square root)
root_square(x,52,plt_mode=True)

# Create subplots
plt.figure()
r = range(49,55)
for iter in r:
    err_max, x, y, yi, yf, inds = root_square(x,iter,plt_mode=False)

    plt.subplot(2,3,iter-48)
    plt.title("iter = %d" % iter)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y,'k--',label='y = x')
    # plt.plot(x,yi,label=r'yi = $x^{\frac{1}{2^{iter}}}$')
    plt.plot(x,yf,'k',label=r'$y_{f}$ = ${(x^{\frac{1}{2^{iter}}})}^{2^{iter}}$')
    plt.plot(x[inds],yf[inds],'r.')
    plt.legend(loc='lower right')
plt.show()

# Max error vs iterations
err = []
r = range(1,60)
for iter in r:
    err_max, x, y, yi, yf, inds = root_square(x,iter,plt_mode=False)
    err.append(err_max)

iters = np.array(r)
err = np.array(err)

log_err = np.log(err)
k = (log_err[50]-log_err[10])/(iters[50]-iters[10])
print(k)

plt.title("Max Error vs. Iterations")
plt.xlabel("Iterations")
plt.ylabel("Max Error")
plt.plot(iters,err,'k.')
plt.yscale('log')
plt.show()
