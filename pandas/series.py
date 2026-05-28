import pandas as pd

dict1={
    'key1':1.2,
    'key2':4.8,
    'key3':3.4
}

series_obj=pd.Series(dict1,['x','y','z'])
print(series_obj)

#check items of series A that are not available in another series B
df1=pd.Series([1,2,43,6])
df2=pd.Series([5,43,6])
df1=df1[~df1.isin(df2)]
print(df1)