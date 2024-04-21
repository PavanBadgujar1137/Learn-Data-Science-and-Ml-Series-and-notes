# scatter - the scatter() function plots one dot for each observation.

'''import matplotlib.pyplot as plt
import numpy as np

x= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,87,87,88,111,86,103,87,94,78,7,85,86])

plt.scatter(x,y)
plt.show()

# now we will compare 2 plots on same figure
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,87,87,88,111,86,103,87,94,78,7,85,86])

plt.scatter(x,y)

# day 2, the age and speed of 
x=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y=np.array([100,105,84,105,90,99,90,95,94,100,79,112,80,85,30])
plt.scatter(x,y)
plt.show()

# now we will set our own color of the marker
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,87,87,88,111,86,103,87,94,78,7,85,86])

plt.scatter(x,y,color='hotpink')

# day 2, the age and speed of 
x=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y=np.array([100,105,84,105,90,99,90,95,94,100,79,112,80,85,30])
plt.scatter(x,y, color='green')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 87, 87, 88, 111, 86, 103, 87, 94, 78, 7, 85, 86])

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange', 'purple', 'gray', 'cyan', 'beige', 'magenta', 'brown']
plt.scatter(x, y, color=colors)

plt.show()

# now we will create a color array, and specify a colormap in scatter plot
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 87, 87, 88, 111, 86, 103, 87, 94, 78, 7, 85, 86])

colors = np.array([0,10,32,13,34,45,3,4,8,87,56,43,23])
plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

# you can also include colorbar in the plot
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 87, 87, 88, 111, 86, 103, 87, 94, 78, 7, 85, 86])

colors = np.array([0,10,32,13,34,45,3,4,8,87,56,43,23])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()

plt.show()

# you can also change the size 

import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 87, 87, 88, 111, 86, 103, 87, 94, 78, 7, 85, 86])

sizes= np.array([20,50,100,200,500,1000,60,60,34,12,50,34,78])
plt.scatter(x, y,s=sizes)

plt.show()

# alpha - you can adjust the traperancy of the dots
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 87, 87, 88, 111, 86, 103, 87, 94, 78, 7, 85, 86])

sizes= np.array([20,50,100,200,500,1000,60,60,34,12,50,34,78])
plt.scatter(x, y,s=sizes, alpha=0.5)

plt.show()'''

# now we will combine color, size and alpha
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors= np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100,size=(100)) 

plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()