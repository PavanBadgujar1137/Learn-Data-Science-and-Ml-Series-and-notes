# build a decision tree classifier model
from sklearn import tree

# define the dataset 
# Dataset: (Outlook, Temperature, Humidity, PlayTennis)
dataset = [
    ("Sunny", "Hot", "High", "No"),
    ("Sunny", "Hot", "High", "No"),
    ("Overcast", "Hot", "High", "Yes"),
    ("Rain", "Mild", "High", "Yes"),
    ("Rain", "Cool", "Normal", "Yes"),
    ("Rain", "Cool", "Normal", "No"),
    ("Overcast", "Cool", "Normal", "Yes"),
    ("Sunny", "Mild", "High", "No"),
    ("Sunny", "Cool", "Normal", "Yes"),
    ("Rain", "Mild", "Normal", "Yes"),
    ("Sunny", "Mild", "Normal", "Yes"),
    ("Overcast", "Mild", "High", "Yes"),
    ("Overcast", "Hot", "Normal", "Yes"),
    ("Rain", "Mild", "High", "No")
]

# Convert categorical data to numerical data 
outlook_mapping = {"Sunny":0, "Overcast":1,"Rain":2}
tempreture_mapping = {"Hot":0, "Mild":1, "Cold":2}
humidity_mapping = {"High":0, "Normal":2}
playTennis_mapping = {"No":0,"High":1}

# iterating over the original dataset
data_numeric = [(outlook_mapping[outlook], tempreture_mapping[temp], humidity_mapping[hum] playTennis_mapping[play]), for outlook,temp,hum,play in dataset]



# step 4 : split the data into features (X) and target variable (y)
X= [x[:-1] for x in data_numeric]
y= [x[:-1] for x in data_numeric]

# now we will create our decision tree classifier
clf=tree.DecisionTreeClassifier()

# train the classifier on the data
clf=clf.fit(X,y)

# predict whether to play tennis or not 
new_data_point = (outlook_mapping["Sunny"],tempreture_mapping["Mild"],humidity_mapping["Normal"])
predicted=clf.predict([new_data_point])

# now map the predicted value back to the original label
predicted_label = [k for k, v in playTennis_mapping.items(), if v == predicted[0]]

# finally print
print("Predicted label for the new data ",predicted_label[0])



