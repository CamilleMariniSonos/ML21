# ML21

<img src="boule_cristal.jpg" height="300">

### Settings

The following environment variables need to be set:  
* `LK_DATABASE_NAME`: name of the postgreSQL database  
* `LK_DATABASE_USER`: user of the postgreSQL database  
* `LK_DATABASE_PASSWORD`: password of the postgreSQL database  

### Current state of the project

* draft of a django project     
* draft of a database structure (in PostGre)  

### Todo

Some ideas:  
- [ ] command to apply all existing scikit learn estimators to solve the problem  
- [ ] view and template to compare the results of the different estimators (and details for each estimators: best parameters)

### Algorithmics
- [ ] Preprocessing : standardization, missing values, etc.
- [ ] Feature engineering : feature selection, feature transformation, signal processing, dimensionality reduction, unsupervised learning
- [ ] Classification and regression : scikit-learn + other libraries (deep learning with theano or tensorflow, gradient boosting with xgboost, etc.)
- [ ] Hyper-parameter optimization : grid-search, random search, heuristics, general purpose global optimization algorithms
- [ ] Combination of multiple algorithms : in series (PCA+SVM -> output) or in parallel (SVM || random forest -> averaged prediction)
- [ ] Automatic detection of the type of data/problem : time-series regression ? image classification ? etc.

### Computing
- [ ] Parallelization 
- [ ] Where are the computations done : locally on the user computer ? on a dedicated server ? on the cloud ? 
- [ ] Do we need funding ? Public or private ?



