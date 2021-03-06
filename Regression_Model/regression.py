# -*- coding: utf-8 -*-
"""Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15pu6VZ9CUohoHZ23iWIjGrtgbr6lClYo
"""

!wget --no-check-certificate \
    https://archive.ics.uci.edu/ml/machine-learning-databases/00294/CCPP.zip \
    -O /tmp/elec-pow.zip

#gets the dataset

import zipfile

zip1 = zipfile.ZipFile('/tmp/elec-pow.zip', 'r')
zip1.extractall('/content')
zip1.close()

#unzips data in content directory

import pandas as pd
columns = ['Temperature', 'Vacuum', 'Pressure', 'Humidity', 'Energy']

raw_data2 = pd.read_excel('/content/CCPP/Folds5x2_pp.xlsx', names=columns)

#panda library extracts data from an excel file

dataset = raw_data2.copy()

dataset.tail()
#prints last 5 rows of the dataset

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_des = train_dataset.describe()
train_des.pop('Energy')
train_des = train_des.transpose()
train_des

#describe the data statistically

train_label = train_dataset.pop('Energy')
test_label = test_dataset.pop('Energy')

#separates the 'answer' from the 'input'

#normalisation function used to normalise the training and test datasets

def norm(x):
  return (x - train_des['mean']) / train_des['std']

norm_train = norm(train_dataset)
norm_test = norm(test_dataset)

print(len(norm_train.keys()))

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.models.Sequential([
  layers.Dense(128, activation='relu', input_shape=[len(train_dataset.keys())]),
  layers.Dense(128, activation='relu'),
  layers.Dense(1)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.RMSprop(0.001), metrics=['mae', 'mse'])

early = keras.callbacks.EarlyStopping(monitor='loss',patience=40)
history = model.fit(norm_train, train_label, epochs=250, verbose=0, callbacks=[early])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

#gets the details of last 5 epochs

loss, mae, mse = model.evaluate(norm_test, test_label, verbose=0)

print("Testing set mean absolute error: {:5.2f}MW energy".format(mae))