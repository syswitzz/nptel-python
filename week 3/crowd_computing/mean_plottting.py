import matplotlib.pyplot as plt
from statistics import mean, median

estimates = [233,384,953,422,123,453, 442,231,323, 234, 453,324, 234,324,545, 643, 435,233,754,232,465,532, 213, 324, 533, 342, 452, 542,563,432,674,135]
estimates.sort()

# trim 10% for accuracy
trim_value = int(len(estimates) * 0.1)
estimates = estimates[trim_value:]
estimates = estimates[:len(estimates)-trim_value]

# generate fake y axis for density mapping
y = list([5 for i in range(1, len(estimates)+1)])


# plotting
plt.plot(estimates, y, "r--")
plt.plot(mean(estimates), 5, "rd")  # the mean of the estimate
plt.plot(median(estimates), 5, "bs")  # the median of the estimate
plt.plot(375, 5, "g^")  # the actual value


plt.show()