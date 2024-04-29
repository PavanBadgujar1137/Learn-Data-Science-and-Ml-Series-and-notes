# iloc: Integer location function which is used on the dataframe., used on indexbased
# dataframe. iloc[row_ind,column]
# Selecting a single element
# val=dataframe.iloc[row,column]
# # Selecting a specific row
# val=datahframe.iloc[row_index]
# This is all code is typed in manually for the understanding

# Selecting a multiple row elements
# val=dataframe.iloc[start_row:end_row]

# # Selecting a multiple row and column elements
# val=dataframe.iloc[[row1,row2],[col1,col2]]

# # Selecting a all rows for specific column
# val= dataframe.iloc[:,[col1,col2]]

# example 
import pandas as pd 
data = {"name": ['pavan','sanjay','piyush','dhanraj'], 'age':[25,23,34,56],'country':['dubai','canada','Uk',"Austrelia"]}
df=pd.DataFrame(data)
print(df)

# Selecting 'Canada'
element=df.iloc[1,2]
print(element)

# Selecting specific rows and column
subset= df.iloc[1:3,0:2]
print(subset)
