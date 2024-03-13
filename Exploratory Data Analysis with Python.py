#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
data_size = 1000
age = np.random.randint(18, 65, data_size)
income = np.random.randint(20000, 100000, data_size)
expenses = np.random.randint(1000, 5000, data_size)
savings = income - expenses + np.random.normal(0, 1000, data_size)

# Create a DataFrame
df = pd.DataFrame({'Age': age, 'Income': income, 'Expenses': expenses, 'Savings': savings})

# Display the first few rows of the DataFrame
print("Generated Data:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize the data
plt.figure(figsize=(12, 8))

# Distribution of Age
plt.subplot(2, 2, 1)
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution')

# Income vs Expenses
plt.subplot(2, 2, 2)
sns.scatterplot(x='Income', y='Expenses', data=df, color='coral')
plt.title('Income vs Expenses')

# Savings Distribution
plt.subplot(2, 2, 3)
sns.histplot(df['Savings'], bins=20, kde=True, color='green')
plt.title('Savings Distribution')

# Correlation Heatmap
plt.subplot(2, 2, 4)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plots
plt.show()


# In[ ]:




