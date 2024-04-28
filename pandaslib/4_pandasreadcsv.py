# read csv files: (comma seperated file) it is a simple way to store the big and biggest data sets. csv file contains plain index. 
# loading the csv file into a datframe with to_strings
import pandas as pd
df=pd.read_csv('tips.csv')
print(df.to_string())

# loading the csv file into a datframe with to_strings
import pandas as pd
df=pd.read_csv('tips.csv')
print(df)

# max_rows : you can check your systems maximum rows with:
import pandas as pds
print(pd.options.display.max_rows)

# yes we can increase the maximum number of rows to display the entire dataframe
import pandas as pd
pd.options.display.max_rows=9999
df=pd.read_csv('tips.csv')
print(df)
