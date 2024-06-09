# Scale Feature : when you data has different value and even the different mesurement unit , than it can be dificult to compare them.so the answer to this problem is scaling or scale feature .

# there are different methods for scalling the data. here we will use the method caled standardization.
# formula of standardization method: 
# z = (x-u)/s where z is the new value , x is the original value, u is the mean and s is the standard deviation.
# now here will scale all the values in the weight and volume columns: 
import pandas 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale =StandardScaler()
df = pandas.read_csv("cars2.csv")
x = df[['Weight','Volume']]
scalex = scale.fit_transform(x)
print(scalex)

# now with the above result we will predict the CO2 emission
# here we will predict the CO2 from a 1.3 lt car that weights 2300 kg.
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
sharad = pandas.read_csv("cars.csv")
x =  df[["Weight","Volume"]]
y=df["CO2"]
scaledx = scale.fit_transform(x)
regr = linear_model.LinearRegression()
regr.fit(scaledx,y)
scaled = scale.transform([[2300,1.3]])
predictedco2 = regr.predict([scaled[0]])
print(predictedco2)