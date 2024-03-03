import multiprocessing
import numpy as np

def fun(data):
    print(data)

nprocess = 10

#len_seq = len(test_img_2)
len_seq = 3231
num = len_seq//nprocess
start_ix = np.arange(len_seq)[::num]
nn = np.zeros(nprocess)
for i in range(len(nn)):
    if i != len(nn) - 1:
        nn[i] = start_ix[i+1] - start_ix[i]
    else:
        nn[i] = len_seq - start_ix[i]

input_data = list(zip(start_ix,nn))
pool = multiprocessing.Pool(nprocess)
pool.map(fun,input_data)
