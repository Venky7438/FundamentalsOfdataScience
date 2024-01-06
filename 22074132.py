import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load data from CSV file
filename = "data2-1.csv"
data = np.loadtxt(filename)

# Calculate mean and standard deviation
mean_salary = np.mean(data)
std_dev = np.std(data)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Salary Distribution')

# Plot the probability density function using a normal distribution
x = np.linspace(min(data), max(data), 100)
pdf = norm.pdf(x, mean_salary, std_dev)
plt.plot(x, pdf, 'k', linewidth=2, label='Normal Distribution')

# Calculate X for the 95th percentile
X_percentile = np.percentile(data, 5)

# Plot vertical lines for mean and X
plt.axvline(mean_salary, color='r', linestyle='dashed', linewidth=2, label='Mean Salary (W)')
plt.axvline(X_percentile, color='b', linestyle='dashed', linewidth=2, label='X (5th Percentile)')

# Add labels, title, and legend
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Salary Distribution Analysis')
plt.legend()

# Print mean and calculated X on the graph
plt.text(max(data), pdf.max() * 0.9, f'Mean (W): {mean_salary:.2f}\nX: {X_percentile:.2f}',
         horizontalalignment='right')

# Display the mean and X in the console
print("Mean Salary (W):", mean_salary)
print("X (5th Percentile) calculation:", X_percentile)

# Show the plot
plt.show()
