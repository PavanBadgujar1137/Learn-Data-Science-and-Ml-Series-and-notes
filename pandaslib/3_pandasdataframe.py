# Dataframe : it is 2D data structure like a 2D array with table incl. rows and coumns.
import pandas as pd
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x)
print(y)

# lacate row: pandas use the loc attribute to return one or more specified row.
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x)
print(y.loc[0])

# example of returning row 0 and 1
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x)
print(y.loc[[0,1,2]])

# named index: with the index arg , you can named your own index
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x,index=["day1","day2","day3"])
print(y)

# locate the named index:
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x,index=["day1","day2","day3"])
print(y.loc["day2"])

# output in a dataframe:
x={"cal":[420,380,390],"duration":[50,40,45]}
y=pd.DataFrame(x,index=["day1","day2","day3"])
print(y.loc[["day1","day2"]])

# load the data from the csv file into dataframe data.csv
import pandas as pd
x=pd.read_csv('data.csv')
print(x)