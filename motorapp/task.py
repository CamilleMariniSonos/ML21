# from __future__ import absolute_import
# from celery import shared_task
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import grid_search
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge
# import sklearn.metrics as skm


def read_data(filename):
    tab = pd.read_csv(filename)
    tab = np.array(tab)
    X = tab[:, 0:-1]
    y = tab[:, -1]
    return X, y


def split_data(X, y, test_size=0.5):
    X_train = X[0: int(X.shape[0] * test_size), :]
    X_test = X[int(X.shape[0] * test_size)::, :]
    y_train = y[0: int(X.shape[0] * test_size)]
    y_test = y[int(X.shape[0] * test_size)::]
    return X_train, X_test, y_train, y_test


def train(model, X_train, y_train, dict_param, cv=5):
    model = grid_search.GridSearchCV(model, dict_param, cv=cv)
    model.fit(X_train, y_train)
    return model


def test(model, X_test, y_test):
    return model.score(X_test, y_test)


# @shared_task
def train_test(filename, pb_type):
    if pb_type == 'CLF':
        dict_param = {'n_estimators': range(12, 142, 10)}
        model = RandomForestClassifier()
    else:
        dict_param = {'alpha': np.logspace(-3, 3, num=7, base=10)}
        model = Ridge()
    X, y = read_data(filename)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.5)
    model = train(model, X_train, y_train, dict_param)
    score = test(model, X_test, y_test)
    return score
