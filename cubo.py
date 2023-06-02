import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax=plt.axes(projection="3d")
z=np.linspace(0,10,100)
x=np.linspace(0,10,100)
y=np.linspace(0,10,100)
mt=[x,y,z]

for o in range(50):
    for i in range(50):
        plt.plot(50,o,i,'o')
        

plt.show()