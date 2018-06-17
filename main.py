import math
import random
import statistics

import matplotlib.pyplot as plt

from BinaryTree import BinaryTree

plot_filename = 'Plot.PNG'
test_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
replications = 100
random.seed(24011994)


def rand():
    return round(random.uniform(0., 1000.), 3)


def generate_points(n):
    return [rand() for _ in range(n)]


def generate_bt(points):
    bt = BinaryTree()
    for p in points:
        bt.add(p)
    return bt


results = {}
for test_size in test_sizes:
    for replication in range(replications):
        print('Executing..', test_size, replication)
        points = generate_points(test_size)
        bt = generate_bt(points)

        if test_size not in results:
            results[test_size] = {}
        results[test_size][replication] = bt.get_height()

print(results)


def compute_results(op):
    return [round(op(results[size].values()), 3) for size in test_sizes]


log_height = [math.log(size, 2) for size in test_sizes]
height_mean = compute_results(statistics.mean)
height_min = compute_results(min)
height_max = compute_results(max)
height_stdev = compute_results(statistics.stdev)

print(height_mean)
print(height_min)
print(height_max)
print(height_stdev)

for i in range(len(test_sizes)):
    print(test_sizes[i], '&', log_height[i], '&', height_mean[i], '&',
          height_min[i], '&', height_max[i], '&', height_stdev[i], '\\\\', '\\hline')

plt.plot(test_sizes, height_mean, c='r')
plt.plot(test_sizes, log_height, c='b')

plt.legend(['Empirical', 'Theoretical'], loc='upper left')

plt.savefig(plot_filename)
plt.show()
