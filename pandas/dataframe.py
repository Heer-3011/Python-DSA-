import pandas as pd

data={'name': ['heer','meet','shobhana'],
       'age':[21,24,43],''
       'city':['ahemdabad','bangalore','surat']
    }
data2={'name': ['priya','riya','leena'],
       'age':[20,30,40],''
       'city':['surat','ahemdabad','surat']
    }
# dataframe have 4 args data,index,coloums=['name','age','city'],Dtype=object
dataframe1=pd.DataFrame(data)
print(dataframe1 ['age'])

dataframe2=pd.DataFrame(data2)
#df1= dataframe.join(dataframe2)
df1_concate=pd.concat([dataframe1,dataframe2])
print(df1_concate)
 
 