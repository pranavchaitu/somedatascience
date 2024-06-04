import matplotlib.pyplot as plt
import numpy as np

# Creating some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating subplots
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plotting data on subplots
axes[0].plot(x, y1)
axes[1].plot(x, y2)

# Adjusting spacing around subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

# Adding titles
axes[0].set_title('Sine')
axes[1].set_title('Cosine')

# Displaying the plot
plt.show()
