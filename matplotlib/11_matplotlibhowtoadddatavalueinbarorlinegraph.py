'''import matplotlib.pyplot as plt
# sample data
categories = ['Category 1','Category 2','Category 3']
values=[20,35,25]

# Create  a bar plot
plt.bar(categories,values)
plt.show()

# add the data points import matplotlib.pyplot as plt
# sample data
import matplotlib.pyplot as plt
categories = ['Category 1','Category 2','Category 3']
values=[20,35,25]

# Create  a bar plot
plt.bar(categories,values)

for i,val in enumerate(values):
    plt.text(i,val ,str(val), ha='center', va='bottom')
plt.show()'''

# Creating a line graph
import matplotlib.pyplot as plt
import numpy as np
x_values = [1,2,3,4,5]
y_values = [10,25,13,32,20]
plt.plot(x_values,y_values,marker='o')
for x,y in zip(x_values,y_values):
    plt.text(x,y,str(y),ha='center',va='bottom')
plt.show()