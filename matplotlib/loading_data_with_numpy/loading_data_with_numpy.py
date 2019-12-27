import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example.txt', delimiter = ',', unpack = True)

plt.plot(x, y, label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Graph')
#plt.show()
plt.savefig('plot.png')
print('Plot saved in `plot.png`. Please click on it to see the graph.')
