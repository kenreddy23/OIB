# -*- coding: utf-8 -*-
"""DL_assign-1-Boston.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11DTdoLhzJmFycMYJai93_i5Z41htDMH8
"""

#  Linear regression by using Deep Neural network: Implement Boston housing
#  price.prediction problem by Linear regression using Deep Neural network. Use Boston House price
#  prediction dataset

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import boston_housing

# Load Boston Housing data using Keras
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

# Standardization
mean, std = X_train.mean(axis=0), X_train.std(axis=0)
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# Linear Regression
lr = LinearRegression().fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("LR RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lr)))
print("LR R2:", r2_score(y_test, y_pred_lr))
print("LR MAE:", mean_absolute_error(y_test, y_pred_lr))

# Deep Neural Network
from keras.layers import Input # Import the Input layer

model = Sequential([
    Input(shape=(13,)),  # Specify input shape here, corrected to 13 for Boston Housing data
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X_train, y_train, epochs=100, validation_split=0.05, verbose=0)

# DNN Evaluation
mse, mae = model.evaluate(X_test, y_test, verbose=0)
print("DNN MSE:", mse)
print("DNN MAE:", mae)

# New prediction
new_sample = [[0.1, 10.0, 5.0, 0, 0.4, 6.0, 50, 6.0, 1, 400, 20, 300, 10]]
new_sample_scaled = (np.array(new_sample) - mean) / std
pred = model.predict(new_sample_scaled, verbose=0)
print("Predicted price:", pred[0][0])