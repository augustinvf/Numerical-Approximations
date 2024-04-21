import numpy as np
import matplotlib.pyplot as plt

# let's use the recursive definition to avoid doing the same calculations twice
def s_n_plus_one(n, sn):
    return sn + ((-1)**(n+1) / (1 + n+1))

NB_POINTS = 10000
FIRST_POINT_TO_DRAW = 100
LAST_POINT_TO_DRAW = NB_POINTS

x = np.arange(NB_POINTS)
y = np.zeros(NB_POINTS)
y[0] = 1

for k in range(1, NB_POINTS):
    y[k] = s_n_plus_one(k-1, y[k-1])

plt.xlabel("n")
plt.ylabel("S_n")
plt.title("Sequence convergent to ln(2)")
plt.scatter(x[FIRST_POINT_TO_DRAW:LAST_POINT_TO_DRAW], y[FIRST_POINT_TO_DRAW:LAST_POINT_TO_DRAW], label='Suite', color='orange', marker='+', s = 1)
plt.show()

print("The approximation of ln(2) is : ", y[NB_POINTS-1])
