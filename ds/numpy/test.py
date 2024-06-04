import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a NumPy array
data = np.array([1, 2, 3, 4, 5])

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=['Numbers'])

# Print the DataFrame
print(df)

# Plot the data
plt.plot(df['Numbers'])
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()
