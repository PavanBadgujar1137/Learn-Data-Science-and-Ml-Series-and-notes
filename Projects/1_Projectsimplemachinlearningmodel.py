# We are creating a simple and easy machine learning model.
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# step 2 for creating random data 
np.random.seed(0)
heights = np.random.normal(160, 10, 100)
weights = 0.6 * heights + np.random.normal(0, 5, 100)
print(heights)
print(weights)

# step 3 Spliting a data for training and testing 
X = heights.reshape(-1,1)
Y = weights
X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

# step 4  : Create and train the linear regration model
model = LinearRegression()
model.fit(X_train, Y_train)

# step 5 : Make prediction using the trained model
y_prediction =  model.predict(X_test)

# step 6 : visualize result
plt.scatter(X_test,Y_test, color='blue', label='Actual Data')
plt.plot(X_test,y_prediction,color='red', label='Regression Line')
plt.xlabel("Height")
plt.ylabel('Weight')
plt.title('Linear Regression: Height Vs Weight')
plt.legend()
plt.show()

