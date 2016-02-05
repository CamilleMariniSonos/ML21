# import pkgutil
import inspect
import sklearn
import json


list_packages = [sklearn.linear_model, sklearn.ensemble, sklearn.svm,
                 sklearn.neighbors]  # , sklearn.kernel_ridge]
# #for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
# for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
#                                                           prefix=package.__name__ + '.'):
#     for pp in list_packages:
#         if pp in modname:
#             print modname, ispkg

estimators_reg = []
estimators_clf = []

for pp in list_packages:
    for name, obj in inspect.getmembers(pp):
        try:
            if inspect.isclass(obj):
                #if 'CV' in name:
                print name
                print obj().get_params()
                for k, v in obj().get_params().items():
                    print type(v)
                if obj._estimator_type == 'regressor':
                    estimators_reg.append([name, obj().get_params()])
                else:
                    estimators_clf.append([name, obj().get_params()])
        except:
            pass

with open('list_estimators.json', 'w') as ff:
    json.dump({'regressor': estimators_reg, 'classifier': estimators_clf}, ff)
