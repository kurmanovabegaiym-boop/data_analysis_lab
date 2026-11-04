import pandas as pd

df = pd.read_csv('ecommerce_orders.csv')

print("--- Exercise 1 ---")
print(df.describe())
total_revenue = df['Revenue'].sum()
avg_order_value = df['Revenue'].mean()
df['Revenue_Growth_Pct'] = df['Revenue'].pct_change()
print(f"Total Revenue: {total_revenue}")
print(f"Average Order Value: {avg_order_value:.2f}")

print("\n--- Exercise 2 ---")
region_category_revenue = df.groupby(['Region', 'Category'])['Revenue'].sum().reset_index()
print(region_category_revenue)

print("\n--- Exercise 3 ---")
order_counts = pd.crosstab(df['Region'], df['Category'])
print("Order Counts Crosstab:")
print(order_counts)

revenue_pivot = pd.pivot_table(
    df, 
    values='Revenue', 
    index='Region', 
    columns='Category', 
    aggfunc='sum', 
    fill_value=0
)
print("\nRevenue Pivot Table:")
print(revenue_pivot)

print("\n--- Exercise 4 ---")
df['RevenueRank'] = df.groupby('Region')['Revenue'].rank(method='dense', ascending=False)
top_3_per_region = df[df['RevenueRank'] <= 3].sort_values(by=['Region', 'RevenueRank'])
print(top_3_per_region[['Region', 'Product', 'Revenue', 'RevenueRank']])

print("\n--- Exercise 5 ---")
df_window = df.copy()
df_window['Order Date'] = pd.to_datetime(df_window['Order Date'])
df_window.set_index('Order Date', inplace=True)
df_window['rolling_avg'] = df_window['Revenue'].rolling(window=3).mean()
print(df_window[['Revenue', 'rolling_avg']].head(10))

print("\n--- Exercise 6 ---")
df_wide = revenue_pivot.copy().reset_index()
df_wide.columns.name = None
df_wide.rename(columns={
    'Apparel': 'Q1_Sales', 
    'Electronics': 'Q2_Sales', 
    'Home Goods': 'Q3_Sales'
}, inplace=True)

df_long = pd.melt(
    df_wide, 
    id_vars=['Region'], 
    value_vars=['Q1_Sales', 'Q2_Sales', 'Q3_Sales'], 
    var_name='Quarter', 
    value_name='Sales'
)
print("Long Format (melt):")
print(df_long.head())

df_wide_again = df_long.pivot(index='Region', columns='Quarter', values='Sales')
print("\nWide Format Again (pivot):")
print(df_wide_again)