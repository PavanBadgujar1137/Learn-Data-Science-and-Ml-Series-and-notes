# Data in a wrong formate: to fix this problem , there are 2 ways: removing the rows or covert all the cells int he same format.

import pandas as pd
x=pd.read_csv('tips.csv')
print(x.to_string())

# now let's try to to convert all the cells in the date column into dates . to_datetime()
import pandas as pd
x=pd.read_csv('tips.csv')
x["Date"]=pd.to_datetime(x['Date'])
print(x.to_string())

# Here now we will remove the rows with a NULL values in the 'Date column.
import pandas as pd
x=pd.read_csv('tips.csv')
x['Date']=pd.to_datetime(x['Date'])
x.dropna(subset=['Date'], inplace=True)
print(x.to_string())