import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024])
revenue = np.array([120, 150, 180, 160, 210])

plt.plot(years, revenue)

plt.title("Annual Revenue")

plt.xlabel("Years")
plt.ylabel("Revenue (by thousands)")

plt.savefig("sample_output.png")
plt.show()
