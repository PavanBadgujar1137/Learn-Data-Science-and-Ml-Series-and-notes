# Multiple regression :  is like the linear tegression but with more thatn independent value, meaning that we try to predict value based on two or more variables: 

# How does the whole process work:
# for this we will start from imporing the Pandas module 
# df =pandas.read_csv("cars.csv")
# then after this we will make a list of indepenedent values and call this variabl x, put the depenedent value in variable called y.
# x=df[['Weight', 'Volume']]
# y=df[CO2']
# now we will use some methods from sklearn module, so se will have to import module as well.
# from sklearn import linear_model
# from sklearn moud;e we will use the Linear regression() method to create a linear regression object.
# this objects has a method called fit() that takes the independent and dependent values as a parameters and fills the regression objects with the data describe the relationship.
# regr= linar_model.LinearRegression() 
# regr.fit(x,y)

# now here we will predict the CO2 of a car where the weight is 2300kg and the volume is 1200
# predictedCO2= regr.predict([[2300,1300]])

# example in action after theory
import pandas 
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)

predictedCO2= regr.predict([[2300,1300]])
print(predictedCO2)

# Coefficient : this is factir that describes the relationship with an unknown variable.
# example : if x is a variable then 2x is x two times . x is unknown and number 2 is the coefficient.

# here we will printt he coefficient value of the regression  boject

import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)

print(regr.coef_)

# explaining the output above:
# [0.00755095 0.00780526] Weight and Volume.
# these values tell us if the weight increage by 1K then CO2 emission increases by 0.00755095 and if the volume increaces by 1, then the CO2 emission increases by 0.00780526

# what if i will increase the weight  with 100kg
import pandas 
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)
# now here we will predict the CO2 of a car where the weight is 3300kg and the volume is 1300
predictedCO2= regr.predict([[3300,1300]])
print(predictedCO2)
