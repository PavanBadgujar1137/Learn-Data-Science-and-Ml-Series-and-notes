# Trigonometric function: numpy provides the ufuncs like sin(), cos(), and tan() that takes values in radian and produce the corresponding sin, cos and tan values.
# here now we will find the sin value of pi/2
import numpy as np
x=np.sin(np.pi/2)
print(x)

# we will now find the sinv values in an array
import numpy as np
x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.sin(x)
print(y)

# Convert Degree into radians: by default all of the trigonometric functions tales radians as parameter.
# note: radians values are pi/180* degree value.
# here we will convert the all the array values to radians:
import numpy as np
x=np.array([90,180,270,360])
y=np.deg2rad(x)
print(y)

# Here wee will cinvert radian t0 degree

import numpy as np
x=np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
y=np.rad2deg(x)
print(y)

# here we can also find the angles: arcsin(), arccos(), and arctan()
# that takes values in radian and produce the corresponding sin, cos and tan values.

# we wull now find then angle of 1.0

import numpy as np
x=np.arcsin(1.0)
print(x)

# angles of each values inn an array:
import numpy as np
x=np.array([1,-1,0.1])
y=np.arcsin(x)
print(y)

# here we can also find the hypoteneous using the pythagoaras theroem in numpy
# hypot() function  that takes values in radian and produce the corresponding sin, cos and tan values.

# Here we will find the hypot for 3 base and 4 perpendicular.
import numpy as np
base = 3
perp= 4
x=np.hypot(base,perp)
print(x)