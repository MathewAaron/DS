from collections import Counter
import numpy as np 

np_array_test = np.array([[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[3,3,3,3,3]])

counter = Counter(np_array_test.flatten().tolist())

assert counter[0] == 5 , "Counter not working"
