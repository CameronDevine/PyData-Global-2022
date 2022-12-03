import numpy as np
import sys
import matplotlib.pyplot as plt

data = np.loadtxt(sys.argv[1], delimiter=";", skiprows=1)

plt.figure()
plt.semilogy(data[:,0], data[:,1], 'bx')
plt.xlabel("Year")

plt.savefig(sys.argv[2])
