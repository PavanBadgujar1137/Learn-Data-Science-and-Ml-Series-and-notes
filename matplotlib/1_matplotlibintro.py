import matplotlib
print(matplotlib.__version__)

# pyplot submodule
# Now we will draw a line in a diagram from a certain position.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([100,600])
ypoints = np.array([50,300])

plt.plot(xpoints,ypoints)
plt.show()