# Random Forest
# example that an email is spam or not - 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# sample dataset 
# features : number of words, Presense of keywords(1 for yes, 0 for no)
x=np.array([[100,1],[50,0],[75,1],[200,1],[30,0],[180,1],[120, 0],[60,1],[90,0],[150,1]])
# labels: 1 for spam , 0 for not spam
y=np.array([1,0,1,1,0,1,0,1,0,1])

# Split the dataset into training and testing data
X_train,X_test,y_train,Y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# Create a Rabdom forest classifier
# n_estimator: This set the number of decision trees in the random forest to 100
rf_classifier = RandomForestClassifier(n_estimators=100,random_state=42)

# Train The Mode; on the training data
rf_classifier.fit(X_train,y_train)
RandomForestClassifier(rf_classifier)

# Making Prediction
y_pred=rf_classifier.predict(X_test)

# Evaluate the model's accuracy (95% above)
accuracy = accuracy_score(Y_test, y_pred) #compare
print(f"Accuracy:{accuracy*100:2f}%")
