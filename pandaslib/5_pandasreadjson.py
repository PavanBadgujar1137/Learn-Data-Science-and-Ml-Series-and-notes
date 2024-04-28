# JSON: Big data sets are normally stored and extracted as JSON. JSON is a plain text, but it has a format of an object.
# Loading the JSONinto a dataframe:
import pandas as pd

data = pd.read_json("data.js")
print(data.to_string())

# Disctionary as a JSON: if your JSON code is not in a file , but in a python dictionary , then you can do all below:
import pandas as pd
data={
    "duration":{"0":60,"1":60,"2":60,"3":45,"4":45,"5":60},
    "pulses":{"0":600,"1":600,"2":600,"3":450,"4":450,"5":600}
}
x=pd.DataFrame(data)
print(x)