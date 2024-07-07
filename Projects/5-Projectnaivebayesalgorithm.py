# naive Bayes algorithm 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

# step 2  : Create a dataset
emails = ["Buy cheap watches now","hi can we rescheduleour meeting", "Congratulations, you have won a prize"," please find the attched report", "Great deals on electrons","Reminder: Dentist appoiment tommorow"]
labels = ["spam","not spam","spam","not spam","spam","not spam"]

# step 3 : 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# step 4 : 
X_train, X_test, Y_train, Y_test = train_test_split(X,labels, test_size=0.3, random_state=43)

# step 5 :
naive_bayes_model =MultinomialNB()
naive_bayes_model.fit(X_train,Y_train)

# step 6 : prediction
y_pred =naive_bayes_model.predict(X_test)

# step & : model evaluation
accuracy = accuracy_score(Y_test,y_pred)
confusion = confusion_matrix(Y_test,y_pred)
report = classification_report(Y_test,y_pred)
print("Accuracy :", accuracy)
print("Confusion matrix: ")
print(confusion)
print("\nClassification Report ;")
print(report)

