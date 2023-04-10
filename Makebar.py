import matplotlib.pyplot as plt
import numpy as np

# Sample data
labels = ['January', 'February', 'March', 'April', 'May', 'June']
values = [20, 35, 30, 25, 40, 45]

# Create figure and axis objects
fig, ax = plt.subplots()

# Set the bar width
width = 0.5

# Create a horizontal bar chart
ax.barh(labels, values, height=width, color='green')

# Set the chart title and axis labels
ax.set_title('Sales by Month')
ax.set_xlabel('Sales')
ax.set_ylabel('Month')

# Invert the y-axis to show the months in descending order
ax.invert_yaxis()

# Add value labels to the bars
for i, v in enumerate(values):
    ax.text(v + 1, i, str(v), color='black')

# Display the chart
plt.show()
