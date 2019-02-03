#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:25:27 2019

@author: sunchuyue
"""
import pdb
import numpy as np
import itertools


from keras.models import Sequential
from keras.optimizers import SGD, Adam
from keras.layers import Conv1D, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.utils import np_utils
from keras.callbacks import Callback
from keras.datasets import mnist
from keras import backend as K
from keras.initializers import VarianceScaling

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.keys = ['loss', 'acc', 'val_loss', 'val_acc']
        self.values = {}
        for k in self.keys:
            self.values['batch_'+k] = []
            self.values['epoch_'+k] = []

    def on_batch_end(self, batch, logs={}):
        for k in self.keys:
            bk = 'batch_'+k
            if k in logs:
                self.values[bk].append(logs[k])

    def on_epoch_end(self, epoch, logs={}):
        for k in self.keys:
            ek = 'epoch_'+k
            if k in logs:
                self.values[ek].append(logs[k])

    def plot(self, keys):
        for key in keys:
            plt.plot(np.arange(len(self.values[key])), np.array(self.values[key]), label=key)
        plt.legend()



def get_data_set(name):
    try:
        data = np.loadtxt(name, skiprows=0, delimiter = ' ')
    except:
        return None, None, None
    np.random.shuffle(data)             # shuffle the data
    # The data uses ROW vectors for a data point, that's what Keras assumes.
    _, d = data.shape
    X = data[:,0:d-1]
    Y = data[:,d-1:d]
    y = Y.T[0]
    print('Loading X', X.shape, 'y', y.shape)
    return X, y



def archs():
    return [[Dense(input_dim=4, units=64, activation='relu'),
             Dense(64, activation="relu"),
             Dense(1, activation = 'sigmoid')],
            [Dense(input_dim=5, units=64, activation='relu'),
             Dense( 64, activation="tanh"),
             Dense(1, activation = 'sigmoid')]]

def run_keras_2d(data_name, layers, epochs, split=0.25, verbose=False, trials=1):
    print('dataset = ', data_name)
    # Load the datasets
    X_train, y_train = get_data_set(data_name)

    val_acc = 0
    for trial in range(trials):
        # Reset the weights
        # See https://github.com/keras-team/keras/issues/341
        session = K.get_session()
        for layer in layers:
            for v in layer.__dict__:
                v_arg = getattr(layer, v)
                if hasattr(v_arg, 'initializer'):
                    initializer_func = getattr(v_arg, 'initializer')
                    initializer_func.run(session=session)
        # Run the model
        model, history = \
               run_keras(X_train, y_train, layers, epochs,
                         split=split, verbose=verbose)
      
      
    if val_acc:
        print ("\nAvg. validation accuracy:"  + str(val_acc/trials))
    print(model)
    return model

    


def run_keras(X_train, y_train, layers, epochs, split=0.25, verbose=True):
    # Model specification
    model = Sequential()
    for layer in layers:
        model.add(layer)
    # Define the optimization
    model.compile(loss='mse', optimizer=Adam(), metrics=['mae', 'mse'])
    N = X_train.shape[0]
    # Pick batch size
    batch = 32 if N > 1000 else 1     # batch size
    history = LossHistory()
    
    # Fit the model
    his = model.fit(X_train, y_train, epochs=epochs, batch_size=batch, validation_split=split,
                  callbacks=[history], verbose=verbose)
    print(his.history)
    # Evaluate the model on validation data, if any
    if history.values['epoch_val_acc']:
        print(history.values)
        val_acc, val_loss = history.values['epoch_val_acc'][-1], history.values['epoch_val_loss'][-1]
        print ("\nLoss on validation set:"  + str(val_loss) + " Accuracy on validation set: " + str(val_acc))

    return model, history 




run_keras_2d('data_test.csv', archs()[0], 1)