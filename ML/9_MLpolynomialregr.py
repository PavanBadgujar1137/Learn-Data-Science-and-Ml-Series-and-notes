# Polynomial Regression: is your data points clearly will not fit a linear regrassion(means straight line), than it might be ideal for a polynomial regression.
# it is also uses relationship between the variables x and y find the bast way draw a line through data point.
# how does it works: here we will register some cars as they were p[assing through certain toolbooth.]
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# plt.scatter(x,y)
# plt.show()

# Now where we will  import numpy and matplotlib and we will drw the line of polynomial 
# import numpy
# import matplotlib.pyplot as plt

# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
# myline=numpy.linspace(1,22,100)
# plt.scatter(x,y)
# plt.plot(myline,mymodel(myline))
# plt.show()

# R - Squared : if here is no relationship in between x and y than polynimial regration cannot predict anything. here the relationship is measured withi the value called R-squared
# R-Sqaured value ranges from p to 1 , where 0 means no relaionship and 1 means 100% related.
# python and the sklearn module will compute this value for you.
# import numpy 
# from sklearn.metrics import r2_score
# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
# print(r2_score(y,mymodel(x)))


# For predicting the future values
# here we will predict the speed of car passing at 17 PM
# import numpy 
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as np
# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
# speed= mymodel(18)
# print(speed)

# What about the BAD fit?
# lets create an example where polynomial regression would not be the best method to prect the future value
# import numpy 
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as plt
# x = [11,2,35,43,5,68,72,80,9,10,13,12,13,14,15,16,17,18]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
# myline=numpy.linspace(2,95,100)
# plt.scatter(x,y)
# plt.plot(myline,mymodel(myline))
# plt.show()

# Its R-Squared value
import numpy 
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
x = [11,2,35,43,5,68,72,80,9,10,13,12,13,14,15,16,17,18]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
print(r2_score(y,mymodel(x)))
