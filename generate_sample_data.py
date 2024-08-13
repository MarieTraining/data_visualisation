import numpy as np
import pandas as pd

# Parameters for normal distribution
mean = 0       # Mean of the distribution
std_dev = 1    # Standard deviation of the distribution
size = 1000    # Number of samples

# Generate normally distributed data
data = np.random.normal(loc=mean, scale=std_dev, size=size)

# Create a DataFrame
df = pd.DataFrame(data, columns=['Value'])

# Save to CSV
csv_file = 'normal_distribution_data.csv'
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")
