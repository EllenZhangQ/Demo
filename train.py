#load iris data from scikit-learn dataset and plot the training data
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

import numpy as np

# load iris data

iris = load_iris()

X = iris.data
Y = iris.target
plt.figure()
