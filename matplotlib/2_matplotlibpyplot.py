# you can use argument marker to emphasize each point with specified marker.
import matplotlib.pyplot as plt
import numpy as np
ypoints= np.array([3,8,1,10])
plt.plot(ypoints, marker='o')
plt.show()

# formate strings "fmt" - marker|line|color
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,'o:r')
plt.show()

# line reference 
# - solid line
# : dotted line
# -- dashed line
# -. dashline/dotted line

# color reference
# r red
# g green
# b blue
# c Cyan
# m magenta
# k black
# w white

# Marker size - ms

import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20)
plt.show()

# marker color  - mec()


import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mec='r')
plt.show()

# Marker face color - mfc

import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20, mec='y', mfc='g')
plt.show()
