import numpy as np
import pandas as pd
from word2number import w2n


'''
reading the file
'''
df=pd.read_csv("Uncleaned_warehouse_data_for_task_1.csv")
# print(df)


'''
analysing the file
'''
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.head())



'''
clean column names
'''
df.columns=df.columns.str.strip().str.replace(" ","_").str.lower()
print(df.columns)


'''
finding duplicates
'''
print(df.duplicated().sum())

'''
standardising
'''
df.replace("NaN",pd.NA,inplace=True)



'''
cleaning quality columns
'''
print(df["quantity"].unique())       #['300', 'two hundred', '100', '50', nan, '150']

df["quantity"]=df["quantity"].apply(lambda x:w2n.word_to_num(x)  if isinstance(x,str) and any(c.isalpha() for c in x )  else x)

# dict={
#     "two hundred":200
# }
# df["quantity"]=df["quantity"].replace(dict)


df["quantity"]=pd.to_numeric(df["quantity"],errors="coerce")
print(df["quantity"].unique())      #[300. 200. 100.  50.  nan 150.]
print(df["quantity"].dtype)            #float64
print(df["quantity"].isnull().sum())     #158
df["quantity"]=df["quantity"].fillna(df["quantity"].mean())
print(df["quantity"].isnull().sum())      #0
print(df["quantity"].unique())       #[300.   200.   100.    50.    161.40142518   150.]


'''
cleaning price columns
'''
print(df["price"].unique())
print(df["price"].isnull().sum())     #207
df["price"]=df["price"].fillna(df["price"].mean())
print(df["price"].isnull().sum())     #0


'''
cleaning last_restocked column
'''
print(df["last_restocked"].unique())
df["last_restocked"]=pd.to_datetime(df["last_restocked"],errors="coerce",dayfirst=True)
print(df["last_restocked"].dtype)
print(df["last_restocked"].unique())
df["last_restocked"]=df["last_restocked"].fillna("Unknown")
print(df["last_restocked"].unique())


'''
saving the cleaned file
'''
df.to_excel("cleaned_warehouse.xlsx",index=False)


new=pd.read_excel("cleaned_warehouse.xlsx")
print(new.info())
print(new.isnull().sum())






