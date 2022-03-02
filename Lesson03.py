# calculate summary stats
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import var
from numpy import std
import numpy as np
import math
import matplotlib.pyplot as plt
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50

# plot distribution
plt.hist(data)
# plt.show()

# calculate statistics
print('Mean numpy function: %.3f' % mean(data))
print('Variance numpy function: %.3f' % var(data))
print('Standard Deviation numpy function: %.3f' % std(data))

# Mean from scratch
sum = 0
for value in data : sum += value
mean_val = sum/len(data)

# Variance from scratch
diff_squared = np.sum([np.power(value - mean_val, 2) for value in data])
var_val = diff_squared/len(data)

# Standard Deviation from scratch
std_val = np.sqrt(var_val)

print(f'Mean from scratch: {round(mean_val, 3)}')
print(f'Variance from scratch: {round(var_val, 3)}')
print(f'Standard Deviation from scratch: {round(std_val, 3)}')


