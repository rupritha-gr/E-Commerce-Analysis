import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. SETUP & DATA LOADING
path = r"C:\Users\rupri\e commerece\e_commerce_electronic_sales_2025_dataset.csv"
df = pd.read_csv(path)

# --- COLUMN ALIGNMENT ---
df.columns = df.columns.str.strip().str.lower()

# Based on your printed columns: ['date', 'order_value', 'quantity']
date_col = 'date'
revenue_col = 'order_value'

# 2. DATA PREPARATION (Fixing the Date Error)
# 'dayfirst=True' solves the ValueError for "19-12-2025"
df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)

# Extract time-based features
df['month'] = df[date_col].dt.month
df['hour'] = df[date_col].dt.hour
df['day_name'] = df[date_col].dt.day_name()

# 3. VISUALIZING PURCHASE PATTERNS
plt.figure(figsize=(15, 6))

# Monthly Sales (Seasonality)
plt.subplot(1, 2, 1)
monthly_sales = df.groupby('month')[revenue_col].sum()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='teal')
plt.title('Monthly Sales Trend (Seasonality)')
plt.xticks(range(1, 13))

# Peak Shopping Hours
plt.subplot(1, 2, 2)
hourly_sales = df.groupby('hour')[revenue_col].sum()
sns.barplot(x=hourly_sales.index, y=hourly_sales.values, color='skyblue')
plt.title('Sales Volume by Hour of Day')
plt.tight_layout()
plt.show()

# 4. SALES FORECASTING PREP (Rolling Average)
daily_sales = df.groupby(date_col)[revenue_col].sum().reset_index()
daily_sales = daily_sales.set_index(date_col).asfreq('D').fillna(0)

# Calculate 7-day Moving Average Trend
daily_sales['moving_avg'] = daily_sales[revenue_col].rolling(window=7).mean()

plt.figure(figsize=(12, 5))
plt.plot(daily_sales.index, daily_sales[revenue_col], label='Actual Daily Sales', alpha=0.4)
plt.plot(daily_sales.index, daily_sales['moving_avg'], label='7-Day Trend Line', color='red', linewidth=2)
plt.title('Daily Sales & Trend Analysis')
plt.legend()
plt.show()

# 5. SEASONAL DECOMPOSITION
# Breaking data into Trend, Seasonality, and Noise

decomposition = seasonal_decompose(daily_sales[revenue_col], model='additive', period=7)
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.show()

# 6. SUMMARY INSIGHTS
print("\n" + "="*30)
print("  PURCHASE PATTERN SUMMARY")
print("="*30)
print(f"Total Transactions: {len(df):,}")
print(f"Total Revenue:      ${df[revenue_col].sum():,.2f}")
print(f"Busiest Day:        {df['day_name'].value_counts().idxmax()}")

print("="*30)
