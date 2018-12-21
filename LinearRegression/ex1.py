# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:59:11 2018

@author: MCS
"""
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from ComputeCost import computeCost
from gradientDescent import gradientDescent
from normalizeData import normalizeData
from normalEquation import normalEquation

data = np.loadtxt('../data/ex1data2.txt', delimiter=',')
X=data[:,0:-1]
#X=normalized(X)
X=normalizeData(X)
X = np.c_[np.ones(data.shape[0]),X]
y =np.c_[data[:,-1]]

#plt.scatter(X[:,1], y, s=30, c='r', marker='x', linewidths=1)
#plt.xlim(4,24)
#plt.xlabel('Variable 1')
#plt.ylabel('Outcome y');
#plt.show()

#print("Cost",computeCost(X, y))




#theta,Cost_J = gradientDescent(X, y)
theta = normalEquation(X, y)
print('theta: ',theta)

#plt.plot(Cost_J)
#plt.ylabel('Cost J')
#plt.xlabel('Iterations')
#plt.show()



#xx = np.arange(5,23)
#yy = theta[0]+theta[1]*xx

# Plot gradient descent
#plt.scatter(X[:,1], y, s=30, c='r', marker='x', linewidths=1)
#plt.plot(xx,yy, label='Linear regression (Gradient descent)')

# Compare with Scikit-learn Linear regression
regr = LinearRegression()
regr.fit(X[:,1:], y.ravel())

#plt.plot(xx, regr.intercept_+regr.coef_*xx, label='Linear regression (Scikit-learn GLM)')
print("intercepr sklear",regr.intercept_)
print("coef sklear",regr.coef_)


print('////////')
print (computeCost(X,y,theta))
#print(Cost_J[-10:-1])

#plt.xlim(4,24)
#plt.xlabel('Population of City in 10,000s')
#plt.ylabel('Profit in $10,000s')
#plt.legend(loc=4)

# Predict profit for a city with population of 35000 and 70000
#print(theta.T.dot([1, 3.5])*10000)
#print(theta.T.dot([1, 7])*10000)


# Create grid coordinates for plotting
#B0 = np.linspace(-10, 10, 50)
#B1 = np.linspace(-1, 4, 50)
#xx, yy = np.meshgrid(B0, B1, indexing='xy')
#Z = np.zeros((B0.size,B1.size))

# Calculate Z-values (Cost) based on grid of coefficients
#for (i,j),v in np.ndenumerate(Z):
#    Z[i,j] = computeCost(X,y, theta=[[xx[i,j]], [yy[i,j]]])

#fig = plt.figure(figsize=(15,6))
#ax1 = fig.add_subplot(121)
#ax2 = fig.add_subplot(122, projection='3d')

# Left plot
#CS = ax1.contour(xx, yy, Z, np.logspace(-2, 3, 20), cmap=plt.cm.jet)
#ax1.scatter(theta[0],theta[1], c='r')

# Right plot
#ax2.plot_surface(xx, yy, Z, rstride=1, cstride=1, alpha=0.6, cmap=plt.cm.jet)
#ax2.set_zlabel('Cost')
#ax2.set_zlim(Z.min(),Z.max())
#ax2.view_init(elev=15, azim=230)

# settings common to both plots
#for ax in fig.axes:
#    ax.set_xlabel(r'$\theta_0$', fontsize=17)
#    ax.set_ylabel(r'$\theta_1$', fontsize=17)

#plt.show()