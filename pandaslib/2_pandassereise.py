# A pandas seriese is like a column in atable. it is 1D array which holds data of any type.
# here we will create a simple pandas series.
import pandas as pd
x=[1,7,2]
y=pd.Series(x)
print(y)

# labeling  - label can be use to access a specified value.
x=[1,7,2]
y=pd.Series(x)
print(y[0])

# with Crate label you can create your own name labels. 
import pandas as pd
x=[1,7,2]
y=pd.Series(x,index=["x","y","z"])
print(y)

# labeling  - label can be use to access a specified value. (aftr creating own label)
x=[1,7,2]
y=pd.Series(x,index=["x","y","z"])
print(y["x"])

# you can also use the key or value object like dictionary, when creating a sereise
# here we will create a simple pandas series from a dictionary .
import pandas as pd
cal = {"day1":420,"day2":380,"daya3":390}
x=pd.Series(cal)
print(x)

# now we will create a serease using only data from day1 and day2
import pandas as pd
cal = {"day1":420,"day2":380,"daya3":390}
x=pd.Series(cal, index=['day1','day2'])
print(x)

# DataFrame : Datasets in pandas are usually multidimensional tables, and they are called dataframes 
# series are like columns and dataframes is the whole table.

# we will now create a dataframe from 2 seriese 
import pandas as pd
x={"cal":[420,380,390], "duration":[50,40,45]}
y=pd.DataFrame(x)
print(y)