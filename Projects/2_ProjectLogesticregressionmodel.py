# create a Logistic Regression model - prdicction of probability
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# step 2 : prepare the data
hours_study = np.array([2,3,5,1,8,10,7,6,4,9])
# 0 for fail, 1 for pass
pass_fail = np.array([0,0,1,0,1,1,1,1,0,1])

# step 3 : spliting of data
X_train,X_test,Y_train,Y_test = train_test_split(hours_study.reshape(-1,1),pass_fail, test_size=0.2, random_state=42)

#  step 4: create and train the model
model = LogisticRegression()
model.fit(X_train,Y_train)

# step 5 : Make Prediction
prediction = model.predict(X_test)


# Evaluate the model
from sklearn.metrics import accuracy_score
acucuracy = accuracy_score(Y_test , prediction)
print("Accuracy",acucuracy)