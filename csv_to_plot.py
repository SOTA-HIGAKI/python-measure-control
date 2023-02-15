import csv
import matplotlib.pyplot as plt

with open('result_with_voltr2.csv', 'r') as f:
    cr = csv.reader(f)
    r = []
    for c in cr:
        r.append(float(c[0]))
    plt.plot(r)
    plt.show()
