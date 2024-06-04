import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
plt.plot(x, y, label='sin(x)')

# Annotate a specific point
plt.annotate(
    'local max',
    xy=(1.5, np.sin(1.5)),
    xytext=(3, 1.5),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave with Annotation')
plt.legend()

# Show plot
plt.show()
