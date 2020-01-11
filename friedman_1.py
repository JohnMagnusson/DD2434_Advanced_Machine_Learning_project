import numpy as np
import math
import rvm_regression as rvm_r
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
from tqdm import tqdm
from sklearn import svm

# Initialize variable
N_pred = 240
dimensions = 10
variance = 0.01
N_test = 1000
N_iter = 100

# Choose kernel between linear_spline or exponential
kernel = "linear_spline"

X_train = np.zeros((N_pred, dimensions)) # Training
for i in range(N_pred):
    for j in range(dimensions):
        X_train[i,j] = np.random.rand()

target_train = (10*np.sin(np.pi*X_train[:,0]*X_train[:,1])
                + 20*pow((X_train[:,2]
                - 1/2), 2) + 10*X_train[:,3]
                + 5*X_train[:,4]
                + np.random.normal(0, 1, N_pred)
                )

X_pred_mean = []
for i in range(N_iter):
    X_pred = np.zeros((N_test, dimensions)) # Test Prediction
    for j in range(N_test):
        for k in range(dimensions):
            X_pred[j,k] = np.random.rand()
    
    X_pred_mean.append(X_pred)

X_pred = np.array(X_pred_mean).mean(axis=0)

true_target = (10*np.sin(np.pi*X_pred[:,0]*X_pred[:,1])
                + 20*pow((X_pred[:,2]
                - 1/2), 2) + 10*X_pred[:,3]
                + 5*X_pred[:,4]
                )

# Fit
alpha, variance_mp, mu_mp, sigma_mp = rvm_r.fit(X_train, variance, target_train, kernel, N_pred)
relevant_vectors = alpha[1].astype(int)

# Predict
target_pred = rvm_r.predict(X_train, X_pred, relevant_vectors, variance_mp, mu_mp, sigma_mp, kernel, dimensions)

# Check Performance
print('RMSE:', sqrt(mean_squared_error(true_target, target_pred)))
print('Number of relevant vectors:', len(relevant_vectors)-1)
plt.scatter(range(N_test), true_target, label='Real')
plt.scatter(range(N_test), target_pred, c='orange', label='Predicted')
plt.legend()
plt.show()

# Performance with SVM from sklearn
clf = svm.SVR()
clf.fit(X_train, target_train)
svm_predict = clf.predict(X_pred)
print('Number of support vectors:', len(clf.support_vectors_))
# Check Performance SVM
print('RMSE for SVM:', sqrt(mean_squared_error(true_target, svm_predict)))
plt.scatter(range(N_test), true_target, label='Real')
plt.scatter(range(N_test), svm_predict, c='orange', label='Predicted')
plt.legend()
plt.show()



