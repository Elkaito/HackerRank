import numpy as np
# Get input
m,n = [int(i) for i in input().strip().split(' ')]
x = []
y = []
for i in range(n):
    data_set = input().strip().split(' ')
    x.append(data_set[:m])
    y.append(data_set[m:])
q = int(input().strip())
features = []
for i in range(q):
    features.append(input().strip().split(' '))
    
# Convert dataset to numpy array   
X = np.array(x,float)
Y = np.array(y,float)
mu_x = np.mean(X)
mu_y = np.mean(Y)
features = np.array(features ,float)
X_hat = X-mu_x
Y_hat = Y-mu_y
# Calculate B
B = np.dot(np.linalg.inv(np.dot(X_hat.T,X_hat)),np.dot(X_hat.T,Y_hat))
# Calculate result
X_new = features-mu_x
Y_new = np.dot(X_new,B)
result = Y_new + mu_y

#print result
for i in result:
    print("%.2f" %i)