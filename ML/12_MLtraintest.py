# in machine learning we crwates a models to predict the outcomes, mesure of the model is good enough or need to rectify, than we use a method called train/test.

# what is tarin/test: 80% for training and 20% testing.
# understanding with a proper data set:
# here for understanding we will use a data set that show 100 customers in shop and their shopping habbits.
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(2)
# sharad1 = np.random.normal(3,1,100)
# sharad2 = np.random.normal(150,40,100)/sharad1
# plt.scatter(sharad1,sharad2)
# plt.show()

# x axis represent the number of minutes before making the purchase and y axis represent the amount of money spent on the purchase

# next is splitting into train/test
# train_x = x[:80]
# train_y = y[:80]
# test_x = x[80:]
# test_y = y[80:]

# how the dispaly the training set:

# plt.scatter(train_x,tain_y)
# plt.show()
'''import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
plt.scatter(train_x,train_y)
plt.show()

#now we will display the testing set:
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
plt.scatter(test_x,test_y)
plt.show()


# what about fit the data set.
# here we will draw polynomial regression through the data point.


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
mymodel= np.poly1d(np.polyfit(train_x,train_y,4))
myline = np.linspace(0,6,100)
plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()

# here we will use R-Squared r2.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
mymodel= np.poly1d(np.polyfit(train_x,train_y,4))


r2 = r2_score(train_y, mymodel(train_x))
print(r2)

# now we will bring the this to testing 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
mymodel= np.poly1d(np.polyfit(train_x,train_y,4))


r2 = r2_score(test_y, mymodel(test_x))
print(r2)'''

# now we will predict the values:
# in the below example we will see how much money will a customer spent if he or she in the shop stay for 5 min
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)
sharad1 = np.random.normal(3,1,100)
sharad2 = np.random.normal(150,40,100)/sharad1
train_x = sharad1[:80]
train_y = sharad2[:80]
test_x = sharad1[80:]
test_y = sharad2[80:]
mymodel= np.poly1d(np.polyfit(train_x,train_y,4))


print(mymodel(5))