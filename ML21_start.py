import sklearn as sk
from sklearn.linear_model import SGDClassifier, Lasso
from sklearn.ensemble import  GradientBoostingClassifier,RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
import numpy as np
import csv
import scipy.io


def load_data():
	# load dataset
	x_train = np.random.random((1000,10))
	y_train = np.sum(x_train,1)>5
	x_test = np.random.random((1000,10))
	return x_train,y_train,x_test

def split_data(X,Y):
	n,p=X.shape
	return X[0:n/2,:],Y[0:n/2],X[1+n/2:,:],Y[1+n/2:]

def metric(y_test,y_pred):
	fpr, tpr, thresholds = sk.metrics.roc_curve(y_test,y_pred)
	return sk.metrics.auc(fpr,tpr)

def run():

	x_train,y_train,x_test = load_data()
	X_train,Y_train,X_test,Y_test = split_data(x_train,y_train)

	best_score_cv = 0
	best_algo = ''

	clf = SGDClassifier(loss="hinge", penalty="l2")
	clf.fit(X_train,Y_train)
	Y_pred = clf.decision_function(X_test)
	if best_score_cv<metric(Y_test,Y_pred):
		best_score_cv = metric(Y_test,Y_pred)
		best_algo = 'hinge + l2'

	for alpha in [0.0001,0.001, 0.01, 0.1]:
		clf= Lasso(alpha=alpha)
		clf.fit(X_train,Y_train)
		Y_pred = clf.decision_function(X_test)
		if best_score_cv<metric(Y_test,Y_pred):
			best_score_cv = metric(Y_test,Y_pred)
			best_algo = 'LASSO with alpha='+str(alpha)

	clf = RandomForestClassifier(n_estimators=1000, max_depth=None, min_samples_split=1, random_state=0)
	clf.fit(X_train,Y_train)
	Y_pred = clf.predict_proba(X_test)
	if best_score_cv<metric(Y_test,Y_pred[:,1]):
		best_score_cv = metric(Y_test,Y_pred[:,1])
		best_algo = 'randomforest with 100 trees'

	print 	
	print 'Thank you for running ML21 futurist meta-algorithm'
	print 
	print '> the best algorithm is : '+best_algo
	print 
	print '> the best cross-validation score is : '+str(best_score_cv)
	print 
	print 'If you want, I can also do your breakfast.'
	print


run()


