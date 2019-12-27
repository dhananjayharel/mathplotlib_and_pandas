from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill')

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()

#plt.show()
plt.savefig('plot.png')
print('Plot saved in `plot.png`. Please click on it to see the graph.')
