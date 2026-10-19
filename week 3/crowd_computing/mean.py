from statistics import mean
from scipy import stats

estimates = [233,384,953,422,123,453, 442,231,323, 234, 453,324, 234,324,545, 643, 435,233,754,232,465,532, 213, 324, 533, 342, 452, 542,563,432,674,135]
estimates.sort()

# trim 10% for better precision
trim_value = int(len(estimates)*0.1)

estimates = estimates[trim_value:]
estimates = estimates[:len(estimates)-trim_value]

print(mean(estimates))


# USING SCIPY

estimates = [233,384,953,422,123,453, 442,231,323, 234, 453,324, 234,324,545, 643, 435,233,754,232,465,532, 213, 324, 533, 342, 452, 542,563,432,674,135]
estimates.sort()

m = stats.trim_mean(estimates, 0.1)

print(m)