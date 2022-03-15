# student's t-test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
# seed the random number generator
seed(1)
# generate two independent samples
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51
# compare samples
stat, p = ttest_ind(data1, data2)
print(f"Statistics = {round(stat, 3)}, p = {round(p, 3)}")
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')


### More statistical tests
# - Wilcoxon Signed-Rank Test
# - Mann-Whitney U Test
# - Kruskal-Wallis Test