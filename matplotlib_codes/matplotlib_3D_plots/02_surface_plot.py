import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fig = plt.figure()
ax = plt.axes(projection = '3d')


##x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
##y = x.copy().T
##z = 0.5 * x**2 + y**2

x = y = np.linspace(-2, 2, 10)
xx, yy = np.meshgrid(x, y)
z = 0.5 * xx**2 + yy**2



ax.plot_surface(xx, yy, z, cmap='viridis', edgecolor='green')
ax.set_title('3D Surface plot ')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
