# -*- coding: utf-8 -*-
"""Task1_classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1urpbYlBxtYiV70CS_z-r1c30WO0bG9w8
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import re
import time
from matplotlib import pyplot as plt
# %matplotlib inline 
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import GridSearchCV

dataset=pd.read_csv('Task1_scrapped_data.csv')
dataset.head()

rowsInData, colsInData = dataset.shape
print("number of rows:" + str(rowsInData) + ", Number of columns:" + str(colsInData))

""".

.

.

# A) Product Classifier
"""

plt.figure(figsize=(15,4))
dataset.Product_Category.value_counts().plot(kind='bar');

"""### It is clear from the plot that our dataset has unbalanced product-category classes, therefore we will not "accuracy score" as our performance metric in later part of evaluation."""

X = dataset.Product_Name
Y = dataset.Product_Category
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,stratify=Y, random_state = 14)

"""## SVM with SGD"""

start1 = time.time()

category_classifier = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=101, max_iter=5, tol=None)),])

category_classifier.fit(X_train, Y_train)

stop1 = time.time()

Y_predicted = category_classifier.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("SVM {liner one} with SGD")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for SVM (liner one) with SGD training: {stop1 - start1}s")

""".

## Improvising SVM with SGD by finding best parameters with help of GridSearchCV
"""

params = {
    'clf__loss' : ['hinge', 'log', 'squared_hinge', 'modified_huber', 'perceptron'],
    'clf__alpha' : [0.0001, 0.001, 0.01, 0.1],
    'clf__penalty' : ['l2', 'l1', 'elasticnet', "none"],
    "clf__max_iter" : [5, 10, 20, 50, 100, 1000]
}

pipe = Pipeline(steps=[('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier())])

grid = GridSearchCV(pipe, param_grid=params, cv=10)

grid.fit(X_train, Y_train)

print(grid.best_params_)

startt = time.time()

category_classifier_final = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l1',alpha=0.001, max_iter=50)),])

category_classifier_final.fit(X_train, Y_train)

stopp = time.time()

Y_predicted = category_classifier_final.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("Modified SVM {liner one} with SGD")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for modified SVM (liner one) with SGD training: {stopp - startt}s")

""".

## Trying SVM and its variants without SGD
"""

start2 = time.time()

clf = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SVC(kernel='linear')),])

clf.fit(X_train, Y_train)
stop2 = time.time()

Y_predicted = clf.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("SVM {liner one}")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for SVM (liner one) without SGD training: {stop2 - start2}s")

"""."""

start3 = time.time()

clf1 = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', LinearSVC(C=1)),])

clf1.fit(X_train, Y_train)
stop3 = time.time()

Y_predicted = clf1.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("linear SVC (equivalent to liner one SVM)")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for linear SVC (equivalent to liner one SVM) without SGD training: {stop3 - start3}s")

"""."""

start4 = time.time()

clf2 = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SVC(kernel='rbf',gamma=0.7,C=1)),])

clf2.fit(X_train, Y_train)
stop4 = time.time()

Y_predicted = clf2.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("SVM {rbf one}")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for SVM (rbf one) without SGD training: {stop4 - start4}s")

"""."""

start5 = time.time()

clf3 = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SVC(kernel='poly',degree=3,C=1)),])

clf3.fit(X_train, Y_train)
stop5 = time.time()

Y_predicted = clf3.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("SVM {polynomial one}")
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

print(f"Training time for SVM (polynomial one) without SGD training: {stop5 - start5}s")

"""### As modified SVM classifier with SGD optimization shows best performance metric, thus we will be using it as our "category classfier" model"""

category_classifier_final.predict(['Mamaearth Onion Hair Oil'])

""".

.

.

# B) Ingredient Predictor
"""

plt.figure(figsize=(18,4))
dataset.Ingredient.value_counts().plot(kind='bar');

"""### It is clear from the plot that our dataset has unbalanced ingredient classes, therefore we will not "accuracy score" as our performance metric in later part of evaluation."""

X = dataset.Product_Name
Y = dataset.Ingredient
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 14)

"""### From discussion happened above we understood that SVM with SGD was best option. So, we will be using it here directly without any comparison. """

params = {
    'clf__loss' : ['hinge', 'log', 'squared_hinge', 'modified_huber', 'perceptron'],
    'clf__alpha' : [1e-3, 0.0001, 0.001, 0.01, 0.1],
    'clf__penalty' : ['l2', 'l1', 'elasticnet', "none"],
    "clf__max_iter" : [5, 10, 20, 50, 100, 1000]
}

pipe = Pipeline(steps=[('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier())])

grid = GridSearchCV(pipe, param_grid=params, cv=10)

grid.fit(X_train, Y_train)

print(grid.best_params_)

startt = time.time()

ingredient_predictor = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='squared_hinge', penalty='elasticnet',alpha=0.01, max_iter=20, random_state = 41))
                                      ])

ingredient_predictor.fit(X_train, Y_train)

stopp = time.time()

Y_predicted = ingredient_predictor.predict(X_test)

score = precision_recall_fscore_support(Y_test,Y_predicted, average='weighted')
score = list(score)
print("weighted precision is "+str(score[0])+", weighted recall is "+str(score[1])+", weighted fscore is "+str(score[2]))

ingredient_predictor.predict(['Mamaearth Onion Hair Oil'])

""".

.

.

# C) Predicting Output
"""

alldetails=[]

for data in X_test:
    name = data
    category = category_classifier_final.predict([name])
    ingredient = ingredient_predictor.predict([name])
    
    temp ={
    'Product_Name':name,
    'Key_Ingredient':ingredient,
    'Product_Category':category}
    
    alldetails.append(temp)
    
dataa = pd.DataFrame(alldetails)
dataa.to_csv('Task1_output_data.csv',index=False)