# linestyle or ls - is used to change the style of plotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints= np.array([3,8,1,10])
plt.plot(ypoints, ls='dashed')
plt.show()

# line color - c

import matplotlib.pyplot as plt
import numpy as np

ypoints= np.array([3,8,1,10])
plt.plot(ypoints, ls='dashed',color="red")
plt.show()
# line width - lw - width of a line


import matplotlib.pyplot as plt
import numpy as np

ypoints= np.array([3,8,1,10])
plt.plot(ypoints, ls='dashed',color="red",lw='20.5')
plt.show()

# example multiple line 

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([6,2,7,11])
ypoints= np.array([3,8,1,10])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()
