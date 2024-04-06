from MachineLearningAlgos.Regression import CustomRegression

import numpy as np

class CustomLinearRegression(CustomRegression):

    def __init__(self):
        super().__init__()
        pass

    def update_wights(self, learning_rate, weight0, weight1):
        weight0 -= learning_rate * weight0
        weight1 -= learning_rate * weight1

    def predict(self, x, w, w0):
        y_hat = x*w + w0

    def squared_loss_error(self, y_hat, y):
        error = np.mean((y_hat - y) ** 2)

    def gradient(self, y, y_hat, x):
        weight0 = -2 * (y - y_hat)
        weight1 = -2 * (y - y_hat) * x

