# cleaning data : it means ffixing the bad data in your data set. bad data could be : empty cell, data in wrong format, duplicate and wrong data.
# empty cell : it will give you wrong result always, we will have to remove the rows always that contain the bad data.
# loading and reading the original dataframe

import pandas as pd
x=pd.read_csv("tips.csv")
print(x.to_string())

# here we will return a new data frame with no empty cell


import pandas as pd
x=pd.read_csv("tips.csv")
y=x.dropna()
print(y.to_string())

# if at any case you want to change the original dataframe, than use the implace=True argument. it will remove the rows containning the NULL(NAN) values.
# import pandas as pd
# x=pd.read_csv("tips.csv")
# y=x.dropna(inplace=True)
# print(y.to_string())

# replacing the empty value : we will use the fillna() method which will aloo us to replace to empty cell with a value.

import pandas as pd
x=pd.read_csv("tips.csv")
x.fillna(130, inplace=True)
print(x.to_string())

# to replace only the empty value for one column, you need to specify the column name.
import pandas as pd
x=pd.read_csv("tips.csv")
x["tip"].fillna(130, inplace=True)
print(x.to_string())

# here we can also the rmpty cell using mean(), median() or mode().
# calculate the MEAN and replace the empty cellvalues with it.
# import pandas as pd
# x=pd.read_csv("tips.csv")
# y=x["tip"].mean()
# y["tip"].fillna(y,inplace=True)
# print(y.to_string())

# calculate the MEDIAN and replace any empty values in it .
import pandas as pd
x=pd.read_csv("tips.csv")
y=x["tip"].median()
y["tip"].fillna(y,inplace=True)
print(y.to_string())

# calculate the MODE and replace any empty values with it .
import pandas as pd
x=pd.read_csv("tips.csv")
y=x["tip"].mode()[0]
y["tip"].fillna(y,inplace=True)
print(y.to_string())