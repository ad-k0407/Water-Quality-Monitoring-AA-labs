
# coding: utf-8

# In[416]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[417]:


df_csv = pd.read_csv("C://Users//shrit//Documents//log_temp.log")
df_csv.head()


# In[418]:


df = pd.read_csv("C://Users//shrit//Documents//log_temp.log")
df.head()


# In[419]:


df = pd.read_csv("C://Users//shrit//Documents//log_temp.log", sep=" ", header=None)
df.head()


# In[420]:


df.columns = ["date", "hour", "temp", "humi"]
df.head()


# In[421]:


df.info()


# In[422]:


df.describe(include="all")


# In[423]:


df["date"].value_counts()


# In[424]:


df["temp"].value_counts()


# In[425]:


df["humi"].value_counts()


# In[426]:


df.info()


# In[427]:


df = df.replace("error",np.NaN)


# In[428]:


df.info()


# In[429]:


df = df.fillna("0000.0")


# In[430]:


df.info()


# In[431]:


df["hour"] = df["hour"].str.slice(stop=2)


# In[432]:


df["temp"] = df["temp"].str.slice(start=2,stop=6)


# In[433]:


df["humi"] = df["humi"].str.slice(start=2,stop=6)


# In[434]:


df.head()


# In[435]:


df.dtypes


# In[436]:


df=df.drop("date",1)
df.head()


# In[437]:


df.reset_index(drop=True,inplace=True)
df.head()


# In[438]:


df.dtypes


# In[439]:


df.temp= df.temp.astype(float)
df.humi = df.humi.astype(float)


# In[440]:


df.dtypes


# In[441]:


df.hour= df.hour.astype(int)


# In[442]:


df.groupby("hour")["temp"].mean().plot(kind="line",color="blue")
df.groupby("hour")["humi"].mean().plot(kind="line",color="orange")


# In[443]:


#Two columns to review
columns = ["temp","humi"]
#Identify the 00.0 as the value to replace
flag = 00.0

#For each two columns, get and save the mean value of the column as a temp value in the case that the first 
#value will be 00.0, otherwise save the first value of the column as a temp value to replace in case of 00.0
for each in columns:
    if df[each].iloc[0] == flag:
        temp_t = df[each].mean()
    else:
        temp_t = df[each].iloc[0]
#In case of 00.0 replace with the temp value, otherwise update the temp value with the current value of the column
    for index, row in df.iterrows():
        if row[each] == flag:
            df.loc[index, each] = temp_t
        else:
            temp_t = df[each].iloc[index]  


# In[444]:


df.describe()


# In[445]:


df.groupby("hour")["temp"].mean().plot(kind="line",color="blue")
df.groupby("hour")["humi"].mean().plot(kind="line",color="orange")

xint2 = np.arange(df["hour"].min(), df["hour"].max()+1, 2)
plt.xticks(xint2)
yint2 = np.arange(df["temp"].min()-2, df["temp"].max()+2, 2)
plt.yticks(yint2)

plt.grid()
plt.title("2019-03-15")
plt.legend(("Temperature","Humidity"))
plt.xlabel("Hour")
plt.ylabel("°C / RH")


# ## Result
# The garph shows observed temp to be between 15C and 33C throughout the day. 
# As we know irriagtion water temperature should vary between 17C to 23C , accord. to the graph irrigation should be
# performed between 12pm to 2.30pm and 6.30am to 8am.
