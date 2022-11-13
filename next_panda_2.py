import numpy as np
import pandas as pd


dict1= {"name":["harry","rohan","skillf","shubh"],
       "marks":[12,24,36,17],
       "city":['rampur','kolkata','bareli','antarctica']}

df=pd.DataFrame(dict1)

df.head()

df.to_csv('friends.csv')

#to remove the index no.
df.to_csv('friends_index_false.csv',index=False)

df.head(2)

df.tail(2)

df.describe()

harry=pd.read_csv('train_main.csv')
harry

harry['speed'][0]=50

harry

harry.to_csv('harry.csv')

harry.index=['first','second','third','fourth']
harry

ser=pd.Series(np.random.rand(33))


type(ser)

newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
newdf

type(newdf)

newdf.describe()

newdf.dtypes

newdf.head()

newdf[0][0]='harry'
newdf.dtypes

newdf.head()

newdf.index

newdf.columns

newdf.to_numpy()

newdf[0][0]=0.3
newdf.head()


newdf.to_numpy()

newdf.T

newdf.head()

newdf.sort_index(axis=0,ascending=False)

newdf.sort_index(axis=1,ascending=False)

newdf.head()

newdf[0]

type(newdf[0])

# newdf2 is the view of newdf
newdf2=newdf

newdf2[0][0]=1544

newdf

newdf2=newdf.copy()

newdf2[0][0]=555

newdf

newdf.loc[0,0]=65

newdf.head(2)

newdf.columns=list("ABCDE")
newdf.head(2)

newdf.loc[0,'A']=65045
newdf.head()

newdf.loc[0,0]=65045
newdf

newdf.drop(0,axis=1)

newdf=newdf.drop(0,axis=1)
newdf.head()

newdf.loc[[1,2],['C','D']]


newdf.loc[:,['C','D']]


newdf.loc[[1,2],:]


newdf.loc[(newdf['A']<0.3)]

newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)]

newdf.head(2)

newdf.iloc[0,4]

newdf.iloc[[0,5],[1,2]]

newdf.head(3)

newdf.drop([0])

newdf.drop(['A','C'],axis=1)

#inplace=true means drop the value in its original place.
newdf.drop(['A','D'],axis=1,inplace=True)
newdf


newdf.drop([1,5],axis=0,inplace=True)
newdf


newdf.head(3)

newdf.reset_index(drop=True,inplace=True)

newdf.head(3)

newdf['B'].isnull()

newdf['B']=55
newdf

newdf.loc[:,'B']=60
newdf.head()

#source:pandas.pydata.org
df=pd.DataFrame({"name":['Alfred','Batman','Catwoman'],
                "toy":[np.nan,'batmobile','bullwhip'],
                "born":[pd.NaT,pd.Timestamp("1942-12-30"),pd.NaT]})
df.head()

df.dropna()

df.dropna(how='all')

df=pd.DataFrame({"name":['Alfred','Batman','Catwoman'],
                "toy":[np.nan,np.nan,np.nan],
                "born":[pd.NaT,pd.Timestamp("1942-12-30"),pd.NaT]})
df.head()

df.dropna(how='all',axis=1)

df=pd.DataFrame({"name":['Alfred','Batman','Alfred'],
                "toy":[np.nan,np.nan,np.nan],
                "born":[pd.NaT,pd.Timestamp("1942-12-30"),pd.NaT]})

df.drop_duplicates(subset='name')


#to keep the value in first ,last,and to remove false.
df.drop_duplicates(subset='name',keep=False)

df.shape

df.info()

#dropna=false means dont remove the na and true means remove the na
df['toy'].value_counts(dropna=False)

df.notnull()

#isnull and notnull is just opposite
df.isnull()

#create a dataframe which contains only integers with 3 rows and 2 columns
#run following dataframe methods on them:
df.describe()
df.mean()
df.chor()
df.count()
df.max()
df.min()
df.median()
df.std()

df=pd.DataFrame(np.arange(1,7).reshape(3,2),index=['row1','row2','row3'],columns=['col1','col2'])

df.head()

df.describe()

df.info()

df.mean()

df.std()

df.max()

df.median()

df.value_counts()

