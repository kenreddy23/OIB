import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# from sklearn.metrics import error_rate
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
df=pd.read_csv('Social_Network_Ads.csv')
print("=======Info========")
print(df)
print("=======Head========")
print(df.head(5))
print("=======Shape========")
print(df.shape)
print("=======isna========")
print(df.isna())
print("=======column========")
print(df.columns)
print("=======isnull========")
print(df.isnull())
print("=======choose features for prediction=======")
X=df[['Age','EstimatedSalary']]
Y=df['Purchased']
print(X)
print(Y)
print("==========Split the data into training and testing sets=========")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("=======x X_train========")
print(X_train.shape)
print("=======Y_train========")
print(Y_train.shape)
print("=======X_test========")
print(X_test.shape)
print("=======Y_test========")
print(Y_test.shape)
print("=========Create a logestic regression model=========")
model=LogisticRegression()
model.fit(X_train,Y_train)
print("=========Predicted values=========")
Y_pred=model.predict(X_test)
print(Y_pred)
print("=========Confusion Matrix=========")
conf_matrix=confusion_matrix(Y_test,Y_pred)
print(conf_matrix)
TN,FP,TP,FN=conf_matrix.ravel()
accuracy=accuracy_score(Y_test,Y_pred)
# error_rate=1-accuracy
precision=precision_score(Y_test,Y_pred)
recall=recall_score(Y_test,Y_pred)
f1=f1_score(Y_test,Y_pred)
print("=========Print values=========")
print("Confusion matrix: ")
print(conf_matrix)
print("True positive: ",TP)
print("True negative: ",TN)
print("False positive: ",FP)
print("False negative: ",FN)
print("Accuracy: ",accuracy)
# print("Error rate: ",error_rate)
print("Precision: ",precision)
print("Recall: ",recall)
print("F1 score: ",f1)
actual = np.random.binomial(1,.9,size = 1000)
predicted = np.random.binomial(1,.9,size = 1000)
confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()
