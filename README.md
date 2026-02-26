E-Commerce Purchase Pattern Analysis & Forecasting (2025)
📌 Project Overview
This project analyzes a dataset of 100K+ electronic sales transactions to identify seasonal buying trends, peak shopping hours, and customer behavioral segments. By leveraging Machine Learning (K-Means) and Time-Series Forecasting (Prophet), the project provides actionable insights for inventory management and targeted marketing.

🛠️ Tech Stack
Language: Python 3.14

Libraries: * Pandas & NumPy (Data Manipulation)

Matplotlib & Seaborn (Data Visualization)

Prophet (Advanced Time-Series Forecasting)

Scikit-Learn (K-Means Clustering)

Statsmodels (Seasonal Decomposition)

Database: SQL (Pattern Extraction & Growth Metrics)

🚀 Key Features
Data Cleaning: Handled inconsistent date formats (D-M-Y) and missing values using robust Pandas preprocessing.

Seasonal Decomposition: Isolated the Trend, Seasonality, and Residuals to understand weekly revenue cycles.

Customer Segmentation: Implemented K-Means Clustering based on RFM (Recency, Frequency, Monetary) metrics to identify high-value customer groups.

Sales Forecasting: Built a Facebook Prophet model to predict revenue for the next 30 days, accounting for holiday spikes.

SQL Analysis: Developed complex queries to calculate Month-over-Month (MoM) growth and peak transactional hours.

📊 Visualizations & Insights
Peak Patterns: Identified that the highest transaction volume occurs between 6 PM and 8 PM.

Seasonality: Detected a 15% lift in weekend sales compared to weekday baselines.

📂 Project Structure
Plaintext
├── data/                   # Dataset (CSV)
├── notebooks/              # Jupyter Notebook with full analysis
├── src/                    # Python scripts for cleaning & modeling
├── sql/                    # SQL queries for MoM growth & KPIs
└── README.md               # Project documentation
📈 Business Impact
Inventory Optimization: Insights allow for better stock allocation during identified peak months.

Targeted Marketing: Customer clusters enable personalized email campaigns for "At-Risk" vs. "VIP" customers.

Data-Driven Forecasting: Provides leadership with a 30-day outlook on projected revenue.
