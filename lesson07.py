# non-parametric = no gaussian distribution
# non-parametric tests ignore the distribution (distribution free methods)
# before applying a non-parametric test, data must be converted into ranked format
# procedure:
# 1. Sort all data in the sample in ascending order.
# 2. Assign an integer rank from 1 to N for each unique value in the data sample.


# example of the mann-whitney u test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import mannwhitneyu
# seed the random number generator
seed(1)
# generate two independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# compare samples
stat, p = mannwhitneyu(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')

# Non-parametric tests
# - Wilcoxon Signed-Rank Test
# - Mann-Whitney U Test
# - Kruskal-Wallis Test
# - Chi-squared test