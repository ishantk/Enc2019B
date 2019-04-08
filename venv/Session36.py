# Clustering in ML
# Unsupervised Learning
# k-means clustering model

import matplotlib.pyplot as plt

"""

    X       Y       P
    -----------------
    1       1       A    
    1       0       B
    0       2       C
    2       4       D
    3       5       E
    
    Step 1:
    We will choose 2 centroids randomly
    eg: Assume A(1,1) and C(0,2) are 2 centroids
    
    Step 2:
    Compute Distance of All the Points from these 2 centroids
    
    Euclilidean Distance Formula :  sqrt[sq(x2-x1) + sq(y2-y1)]
    
    P   C1(1,1) C2(0,2)
    -----------------------
    A    0      1.4                   
    B    1      2.2
    C    1.4    0       
    D    3.2    2.8    
    E    4.5    4.2
    
    Step 3:
    Arrange points according to distance from centroids
    A    C1
    B    C1
    C    C2
    D    C2
    E    C2
    
    Step 4:
    Re-Check again with new Centroid Means
    
    X       Y       P
    -----------------
    1       1       A    
    1       0       B
    0       2       C
    2       4       D
    3       5       E
    
    CM1 = (1+1)/2 , (1+0)/2         =>  1,   .5
    CM2 = (0+2+3)/3 , (2+4+5)/3     =>  1.7, 3.7
    
    P   CM1(1,.5) CM2(1.7,3.7)
    -----------------------
    A   .5         2.7            
    B   .5         3.7 
    C   1.8        2.4        
    D   3.6        0.5       
    E   4.9        1.9
    
    Arrange points according to distance from centroids means
    A    CM1
    B    CM1
    C    CM1
    D    CM2
    E    CM2    
    
    Redo the same steps again
    
    
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
    
"""

X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]

plt.xlabel("X")
plt.ylabel("X")
plt.scatter(X,Y)
plt.savefig("k-means")
plt.show()

