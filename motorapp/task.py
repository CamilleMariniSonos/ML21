# from __future__ import absolute_import
# from celery import shared_task
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skm


def read_data(filename):
    tab = pd.read_csv(filename)
    tab = np.array(tab)
    X = tab[:, 0:-1]
    y = tab[:, -1]
    return X, y


def split_data(X, y, test_size=0.5):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=test_size,
                                                        random_state=142)
    return X_train, X_test, y_train, y_test


def train(X_train, y_train):
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf


def test(X_test, model):
    return model.predict(X_test)


def evaluate(y_test, y_pred):
    return skm.accuracy_score(y_test, y_pred)


# @shared_task
def train_test(filename, pb_type):
    X, y = read_data(filename)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.5)
    clf = train(X_train, y_train)
    y_pred = test(X_test, clf)
    score = evaluate(y_test, y_pred)
    return score
