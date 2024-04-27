# ufunction - stands for univrsal function and they are numpy function thet operates on the ndaaray objects.
# ufunction also take addition arguments like , where , dtype and out
# vectorization - coverting the iterative statement into a vector based statement.
# example without ufunction - here we wil use python in build zip(.)

x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i,j in zip(x,y):
    z.append(i+j)

print(z)

# with ufunction, we will now use add() function 
import numpy as np
x=[1,2,3,4]
y=[4,5,6,7]
z=np.add(x,y)