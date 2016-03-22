# import pkgutil
import inspect
import sklearn
import sklearn.linear_model
import sklearn.ensemble
import sklearn.svm
import sklearn.neighbors
import json


list_packages = [sklearn.linear_model, sklearn.ensemble, sklearn.svm,
                 sklearn.neighbors]  # , sklearn.kernel_ridge]

estimators_reg = []
estimators_clf = []

for pp in list_packages:
    pp_string = str(pp).split(".")[1].split("'")[0]
    for name, obj in inspect.getmembers(pp):
        try:
            if inspect.isclass(obj):
                print name
                print obj().get_params()
                for k, v in obj().get_params().items():
                    print type(v)
                if obj._estimator_type == 'regressor':
                    estimators_reg.append([pp_string, name,
                                           obj().get_params()])
                else:
                    estimators_clf.append([pp_string, name, obj().get_params()])
        except:
            pass

with open('list_estimators.json', 'w') as ff:
    json.dump({'regressor': estimators_reg, 'classifier': estimators_clf}, ff)
