import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('insurance.csv')

print("--- Data Preview ---")
print(df.head())


# How much more do smokers pay on average?
smoker_costs = df.groupby('smoker')['charges'].mean()
penalty = smoker_costs['yes'] - smoker_costs['no']
print(f"\nAverage extra cost for smokers: ${penalty:.2f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['charges'], c=df['bmi'], cmap='viridis', alpha=0.5)
plt.colorbar(label='BMI')
plt.title('Insurance Charges vs Age (Colored by BMI)')
plt.xlabel('Age')
plt.ylabel('Annual Charges ($)')


plt.savefig('insurance_chart.png')
print("\nSuccess! 'insurance_chart.png' has been created.")
plt.show()
