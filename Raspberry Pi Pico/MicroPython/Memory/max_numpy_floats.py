import gc
import numpy as np
gc.collect()
start = gc.mem_free()/1000

for ii in range(100, 100000, 100):
    gc.collect()
    xx = np.zeros(
        (1,ii), 
        dtype = np.float
        )
    print(
        '#floats:',ii,
        'Size:', start - gc.mem_free()/1000,
        'Space left:', gc.mem_free()/1000
        )