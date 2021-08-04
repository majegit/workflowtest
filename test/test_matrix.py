import numpy as np
import matrix

def test_matrixMultiplication():
    a = np.array([1,2])
    b = np.array([1,2])
    assert matrix.matrixMultiplication(a,b) == [5]
