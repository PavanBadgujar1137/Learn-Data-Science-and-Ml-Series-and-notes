# Viewing the data : one of the most used method for a quick overview of the dataframe is the head() memthod. this method returns the headers and specified number of rows.
# here we will print the first 10 rows in the dataframe.
import pandas as pd
x=pd.read_csv("tips.csv")
print(x.head(10))

# here we will print the last 10 rows in the dataframe.
import pandas as pd
x=pd.read_csv("tips.csv")
print(x.tail(10))

#what if you want the information about the data in the dataframe:
import pandas as pd
df=pd.read_csv("tips.csv")
print(df.info())