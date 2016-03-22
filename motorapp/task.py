# from __future__ import absolute_import
# from celery import shared_task
import json
import numpy as np
import pandas as pd
import sklearn
# from sklearn.cross_validation import train_test_split
from sklearn import grid_search
import sklearn.linear_model
import sklearn.ensemble
import sklearn.svm
import sklearn.neighbors


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
    X, y = read_data(filename)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.5)
    with open('list_estimators.json', 'r') as ff:
        sklearn_estimators = json.load(ff)
    dict_problem = {'CLF': 'classifier', 'REG': 'regressor'}
    dict_score = {}
    for estimator in sklearn_estimators[dict_problem[pb_type]]:
        if 'CV' in estimator[1]:
            model = getattr(getattr(sklearn, estimator[0]), estimator[1])()
            # dict_all_param = estimator[2]
            # model = train(model, X_train, y_train, dict_param)
            model.fit(X_train, y_train)
            score = test(model, X_test, y_test)
            dict_score[estimator[1]] = score
    return dict_score
