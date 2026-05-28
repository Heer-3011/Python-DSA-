import pandas as pd
import numpy as np

data={'name': ['heer','meet','shobhana'],
       'age':[21,24,43], 
       'city':['ahemdabad','bangalore', None]
    }

df=pd.DataFrame(data)
print(df)
missing_data_count=df.isnull().sum() #return either true or false 
print(missing_data_count)

missing=df.isna()
print(missing)

#replacing missing values
df['city']=df['city'].fillna(0)
print(df)