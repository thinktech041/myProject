import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap



# IMPLEMENTING IT WITH CLASSES AND OBJECTS

class ChessBoard():
    pass




Ourboard = np.tile([1,0],(8,4))

for i in range(Ourboard.shape[0]):
    Ourboard[i]=np.roll(Ourboard[i], i%2)

cmap = ListedColormap(['#779556','#ebfcd0'])
plt.matshow(Ourboard, cmap=cmap,)
plt.xticks([])
plt.yticks([])
plt.show()

