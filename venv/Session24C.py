import matplotlib.pyplot as plt

# Define Size of Graph
# plt.figure(figsize=(6,6))

jobs = [120, 80, 60]
domains = ["IT", "Marketing", "Accounts"]

plt.pie(jobs, labels=domains)
plt.legend()
plt.show()