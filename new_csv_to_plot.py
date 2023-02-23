import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cr = pd.read_csv("0215_6.csv")
r, s, t, u = cr
s = s - statistics.mean(s)
t = np.array(t)
t = t - statistics.mean(t)
u = np.array(u)
u = u - statistics.mean(u)
plt.plot(r, s, label="R")
plt.plot(r, t, label="X")
plt.plot(r, u, label="Y")
plt.legend()
plt.show()