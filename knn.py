import numpy as np
from random import randint

import matplotlib.pyplot as plt
def create_dataset():
    group = np.random.random((100,2))
    lables = ["o","."]

    lable = [ lables[1 - (g[0]+g[1]).__round__()]  for g in group]
    return group, lable


ds, lables = create_dataset()
print(ds)
def plot():
    x, lable = create_dataset()
    for i in range(lable.__len__()):
        plt.plot(x[i,0],x[i,1],lable[i])
    
    plt.show()


def vote():
    pass


def classify(inX, dataset, lables, k):
    datasetSize = dataset.shape[0]
    diffMatrix = np.tile(inX,(datasetSize,1)) - dataset
    sqDiff = diffMatrix**2
    sqdistsum = np.sum(sqDiff, axis=1)
    distances = sqdistsum**0.5
    sort = distances.argsort()
    print(sort)
    classes = {}
    for i in range(k):
        classes[lables[sort[i]]] = classes.get(lables[sort[i]],0) +1


    clas = [x for x in classes]
    votes = [classes[x] for x in classes]
    sorted_votes = np.argsort(votes)

    print(votes,clas)

    plt.plot(inX[0],inX[1],clas[sorted_votes[-1]],data="classified",scalex=0.1,scaley=0.1)
    plot()
    plt.show()
    
plot()