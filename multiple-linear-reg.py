import copy, math
import numpy as np
import matplotlib.pyplot as plt
"""
df= pd.read_csv("algae_dataset.csv")
print(df.head())
df=df.drop(columns="filter_percent")
print(df.head())
x=df.to_numpy()
w=np.zeros(x.shape)
b=np.zeros(w.shape)
alpha = 0
w_copy=0
#f=np.dot(w,x) + b
def gradiant_descent(w,x,b):
    for i in range(w.shape[0]):
        for j in range(0,i):
            w_copy= w[i,j] - alpha * (((1/w.shape[0])*(np.dot(w[i,j],x[i,j]) + b) - x[5,i])*x[i,j])
            b= b - alpha*((1/w.shape[0])*(np.dot(w[i,j],x[i,j]) + b) - x[5,i]) """





X_train = np.array([[2104, 5, 1, 45],
                    [1416, 3, 2, 40],
                    [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])
b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
def cost(x,y,w,b):
    m= x.shape[0]
    cos = 0
    for i in range(m):
        cos = cos + ((np.dot(x[i],w) + b) - y[i])**2
    cos = cos / (2*m)
    print(cos)
cost(X_train,y_train,w_init,b_init)

def des(x,y,w,b):
    m = x.shape[0]
    n= x.shape[1]
    print(m , n)
    dj_dw = np.zeros((4,))
    dj_db = 0
    print(dj_dw[0])
    error = 0 
    for i in range(m):
        error =  (np.dot(w,x[i])+b - y[i])
        for j in range(n):
            dj_dw[j] =dj_dw[j]+ error * x[i,j]
        dj_db = dj_db + error                       
    dj_dw = dj_dw / m                                
    dj_db = dj_db / m  
    return(dj_dw , dj_db)

aa,bb=des(X_train,y_train,w_init,b_init)
print(aa,bb)
def gradient_des(x,y,w,b,cost,grad,alpha,no):
    m=x.shape[0]
    w1=copy.deepcopy(w)
    dw,db = grad(x,y,w,b)
    for i in range(no):
        

        w = w - alpha*dw
        b= b -   alpha*db
    return w, b



