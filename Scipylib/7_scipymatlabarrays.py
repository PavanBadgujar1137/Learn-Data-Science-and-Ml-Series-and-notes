# Scipy matlab Arrays: Exporting the data in Matlab format
# for converting or export data we use savemat()
# have 3 Parameters: filename,mdict,do_compression.

# example: here now we will export the below array as  variable name "vec" to mat file.
from scipy import io
import numpy as np
x= np.arange(10)
io.savemat('x.mat', {"vec":x})

# here now we will import the existing  mat file. it have only one paameter  that is filename
from scipy import io
import numpy as np
x=np.array([0,1,2,3,4,5,6,7,8,9])
io.savemat('x.mat',{"vec":x})
#import 
x_new=io.loadmat('x.mat', squeeze_me=True)
print(x_new['vec'])

