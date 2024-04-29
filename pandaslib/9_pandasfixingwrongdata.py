# wrong data :  its only a wrong data

# loading and reading the original dataframe

import pandas as pd
x=pd.read_csv("tips.csv")
print(x.to_string())

# here we will set "Duration" = 45 in row 7:
# loading and reading the original dataframe

import pandas as pd
x=pd.read_csv("tips.csv")
x.loc[7,'Duration']=45
print(x.to_string())

# for larger data set: now here we will loop through all the values in "Duration" column, if the value is higher thatn 120 than set it to 120 .
import pandas as pd
x=pd.read_csv("tips.csv")
for i in x.index:
    if x.loc[i,"Duration"] >120:
        x.loc[i,"Duration"]= 120
print(x.to_string())


# You can also remove the rows from wrong data in larger data set.
import pandas as pd
x=pd.read_csv("tips.csv")
for i in x.index:
    if x.loc[i,"Duration"] >120:
        x.drop(i,inplace=True)
print(x.to_string())