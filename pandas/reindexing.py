# Changing row labels (index) or column labels of a DataFrame.
# Add new indexes
# Remove indexes
# Rearrange indexes

import pandas as pd

data={'name': ['heer','meet','shobhana'],
       'age':[21,24,43], 
       'city':['ahemdabad','bangalore','surat']
    }

df=pd.DataFrame(data) 
df_reindex=df.reindex([2,0,1]) #it doesnt rename just reindex the data
# print(df_reindex)

df_columns=df.reindex(columns=['age','city','name'])
# print(df_columns)

#new column to the dataframe
df['third']=pd.Series([10,20,30],index=['a','b','c'] )    
print (df)   

#delte the row or column
df.drop(labels=['third'],axis=0)
print(df)