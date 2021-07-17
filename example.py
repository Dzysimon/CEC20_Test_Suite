from CEC20_Test_Suite import *

cec1 = CEC20_Test_Suite(1)
x = np.array([[0.0] * 10, [1.0] * 10, [1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 0]], dtype=np.float64) # type of data should be set as np.float64
r = cec1.func(x)
print(r)