import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np

with open('0215_7_手動θF.csv', 'r') as f:
    cr = csv.reader(f)
    r = []
    # s = []
    # t = []
    # u = []
    for c in cr:
        r.append(float(c[0]))
        # s.append(float(c[1]))
        # t.append(float(c[2]))
        # u.append(float(c[3]))
    r = np.array(r)
    # s = np.array(s)
    # s = s - statistics.mean(s)
    # t = np.array(t)
    # t = t - statistics.mean(t)
    # u = np.array(u)
    # u = u - statistics.mean(u)
    # plt.plot(r, s, label="R")
    # plt.plot(r, t, label="X")
    # plt.plot(r, u, label="Y")
    # plt.legend()
    plt.plot(r)
    plt.show()
