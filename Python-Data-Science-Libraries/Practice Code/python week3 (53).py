# numpy random numbers,reproducibility & performance tips:
# seed:is an initial value that helps determine the sequnece of random numbers
import numpy as np
rng=np.random.default_rng()
# 0 for tails 1 for head
flips=rng.integers(0,2,size=1000)
prob_head=np.mean(flips)
print("the estemated probabality of head is: ",prob_head)



# now jab hm ye uper wala program jitna run kerty uske value of probality kam hti jaege
# run kerny ke bad tu uske liye take probality value maintain rahy hm use kerty hy seed
# ka functiobn lets see kase kamm kerta hy

import numpy as np
rng=np.random.default_rng(seed=43)
flips=rng.integers(0,2,size=1000)
prob_head=np.mean(flips)
print("the estimated probality of head is :",prob_head)



# python loop time
import time
start=time.time()
square=[i**2 for i in range(1000000)]
end=time.time()
print("loop time:",end-start)

# vectorized time
start=time.time()
arr=np.arange(1000000)
squares_np=arr**2
end=time.time()
print("vectorized time is",end-start)

