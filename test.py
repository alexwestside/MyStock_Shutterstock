a = [0, 5.22, "A", "Tue", 1.2]
b = [8, 10]
a[1:3] = [8, 10]
print(a)

p = 6
q = 2
print(p * q)

import numpy as np
z = np.array([[3, 4, 2],
              [3, 2, 8]])
print(z[0, 0])

import numpy as np
x = np.array([1, 2, '3.0'])
print(type(x))

import numpy as np
x = np.array([5, 7, 7, 4, 6, 6, 4, 4])
y = np.array([8, 2, 1, 8, 4, 5, 5, 9])
print(np.corrcoef(x, y))

x = [2, 1, -4, 3, -1, 5]
print(x[-6])

import numpy as np
costs = np.column_stack(([3, 3, 3, 2, 3, 2, 1, 2],
                         [4, 5, 4, 4, 7, 6, 6, 5]))

cost = costs[0:1]
mean_costs = np.mean(costs[0:,1])
print(mean_costs)

x = [5, 15, 12, 7, 12, 0]
print(x[3:5])

x = [1, 4, 7, 5, 8]
x[3:4] = []
print(x)

import numpy as np
x = np.array([4, 26, 16, 0])
y = np.array([12, 27, 22, 18])
z = np.column_stack([x, y])
print(z.shape)