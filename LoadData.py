# Description: Load data from scikit-learn dataset and plot the training data
# Author: Qing Ellen Zhang  
# Last Update: 04/20/2015


# load iris data from scikit-learn dataset and plot the training data
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# load iris data
iris = load_iris()
X = iris.data
y = iris.target
# plot the training data
#
plt.figure()
# plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Training data')
plt.show()



