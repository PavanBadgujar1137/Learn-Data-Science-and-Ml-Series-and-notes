# Removing the duplicates values:  if first you need to discover the duplicate values via duplicate()

# loading and reading the original dataframe
import pandas as pd
x=pd.read_csv("tips.csv")
print(x.to_string())

# returns True for every row that is duplicate otherwise return false:
import pandas as pd
x=pd.read_csv("tips.csv")
print(x.duplicated().to_string())

# removing the duplicate from the data set. via drop_duplicates()
import pandas as pd
x=pd.read_csv("tips.csv")
x.drop_duplicates(inplace=True)
print(x.to_string())