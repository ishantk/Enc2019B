"""

    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    Equation of Line:
    Y = b0 + b1X
    We need to find value of b0 and b1

    Step1:
    -----------------------------------------------
    X   Y   X-MX    Y-MY    Sq(X-MX)  (X-MX)(Y-MY)
    -----------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    ----------------------------------------------


    Mean of X -> MX : 3
    Mean of Y -> MY : 4

    Step2:
    Sum of Sq(X-MX)     : 10
    Sum of (X-MX)(Y-MY) : 6

    b1 = (X-MX)(Y-MY) / Sq(X-MX)
    b1 = 6/10
    b1 = 0.6

    Y = b0 + (0.6)X

    Step3:

    Put X and Y mean values in Equation to get b0
    4 = b0 + (0.6)(3)
    b0 = 2.2

    Equation of Line with b0 and b1 values:
    =================
    Y = 2.2 + (0.6)X
    =================

    Step4:
    Calculate Square Mean Error (SME) or Mean Square Error (MSE)

    Substitute original value of X to gey Y' as new Predicted Output

    -----------------------------------------------
    X   Y   Y'   (Y-MY) Sq(Y-MY) (Y'-MY)  Sq(Y'-MY)
    -----------------------------------------------
    1   2   2.8    -2     4     -1.2        1.44
    2   4   3.4     0     0     -0.6        0.36
    3   5   4       1     1       0          0
    4   4   4.6     0     0     0.6         0.36
    5   5   5.2     1     1     1.2         1.44
    ----------------------------------------------

    MSE = Sum of Sq(Y'-MY) / Sum of Sq(Y-MY)
    MSE = 3.6 / 6
    MSE = 0.6

    MSE is in the range of 0 to 1

    Class Assignment : Code the above explained Algo in Python
    Project Task     : 1. Predicting Share Prices (Read CSV Files / WebScrap and Create SCV and Read)
                       2. Predicting Student Assessment
                       3. Sports
"""


