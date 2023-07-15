#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Task 1: To train a machine learning model that can learn from the measurements of the 
            iris species and classify them into three different species(setosa, versicolor, and virginica)"""


import numpy as np   #numpy is used for linear algebra
import pandas as pd   #pandas is used for operations on csv files
import matplotlib as plt  #matplotlib is used for creating pie charts, histogram, etc
import seaborn as sns   #seaborn is used for visualisation of data. It is build on top of matplotlib


# In[2]:


df=pd.read_csv('/Users/nitish/internship_task/Iris.csv')   #reading or importing the file


# In[3]:


df.head(15)  #Here we are displaying first 15 rows of our Iris.csv file to check if file has successfully read


# In[4]:


df=df.drop(columns=['Id'])  #we will drop 'Id' column as we already have default index for our data


# In[5]:


df


# In[6]:


df.count()   #here we calculated total flowers in each columns


# In[7]:


df.Species.value_counts()   #here we found out the number of flowers in each species


# In[8]:


df.shape  #using .shape we can find number of rows and columns in the given dataset


# In[9]:


df["Species"].replace({"Iris-setosa": 2, "Iris-versicolor": 3, "Iris-virginica": 4}, inplace=True)  

#We will replace our three unique species with numbers to make calculations and representation easy


# In[10]:


df.head(10)   #we are checking if values are replaced 


# In[11]:


x=pd.DataFrame(df,columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]).values
y=df.Species.values.reshape(150,1)   #Here we are creating two arrays 'x' for flower dimensions and 'y' for species


# In[12]:


x


# In[13]:


y


# In[19]:


#Now we will train a model with above data

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings     #warnings package is used for control of warnings(ie if to ignore them, or to display them)
import matplotlib.pyplot as plt      


# In[15]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)


# In[16]:


k=7
clf=KNeighborsClassifier(k)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)


# In[17]:


metrics.accuracy_score(y_test,y_pred)*100


# In[21]:


import matplotlib.pyplot as plt

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the predicted labels
ax.plot(y_test, label='Actual')

# Plot the actual labels
ax.plot(y_pred, label='Predicted')

# Set labels and title
ax.set_xlabel('Sample index')
ax.set_ylabel('Label')
ax.set_title('Predicted vs Actual Labels')

# Add a legend
ax.legend()

# Show the plot
plt.show()



# In[ ]:




