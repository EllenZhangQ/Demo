# Description: This file contains the code for the training of the model

# load iris data from scikit-learn dataset and plot the training data

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# load iris data
iris = load_iris()
X = iris.data
y = iris.target

# plot the training data
plt.figure()

# plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)







