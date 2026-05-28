import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Data Loading
sales_data = pd.read_excel('Supermarket-Sales-Sample-Data.xlsx', header = None)

print(sales_data.head(15))

# Reloading data with correct header
sales_data = pd.read_excel('Supermarket-Sales-Sample-Data.xlsx', header = 7)
print(sales_data.head(15))

# remove the unnamed columns
sales_data = sales_data.drop(columns = ['Unnamed: 0'])
print(sales_data.head(15))

# first 5 rows of the data
print("\n===== First 5 rows of the data =====")
print(sales_data.head(5))

# last 5 rows of the data
print("\n===== Last 5 rows of the data =====")
print(sales_data.tail(5))

# information about the data
print("\n===== Information about the data =====")
print(sales_data.info())

# dataset shape
print("\n===== Dataset shape =====")
print(sales_data.shape)

# summary statistics of the data
print("\n===== Summary statistics of the data =====")
print(sales_data.describe())

# check for missing values
print("\n===== Check for missing values =====")
print(sales_data.isnull().sum())

# check for duplicate values
print("\n===== Check for duplicate values =====")
print(sales_data.duplicated().sum())

# Final data after cleaning
print("\n===== Final Data after Cleaning =====")
print(sales_data.head(15))

# Columns Name Check
print("\n===== Columns Name Check =====")
print(sales_data.columns.tolist())

# Business KPI analysis

# total sales
total_sales = sales_data['Total (USD)'].sum()
print("\n===== Total Sales =====")
print(total_sales)

# avarage order value or avarage sales per transaction
average_order_value = sales_data['Total (USD)'].mean()
print("\n===== Average Order Value =====")
print(average_order_value)

# Highest order value
highest_order_value = sales_data['Total (USD)'].max()
print("\n===== Highest Order Value =====")
print(highest_order_value)

# lowest order value
lowest_order_value = sales_data['Total (USD)'].min()
print("\n===== Lowest Order Value =====")
print(lowest_order_value)

# Customer with heighest spending
top_customer = sales_data.sort_values(by = 'Total (USD)', ascending = False)
print("\n===== Top Customer =====")
print(top_customer[['Customer Name', 'Total (USD)']].head(10))

# Revenue by customer
revenue_by_customer = sales_data.groupby('Customer Name')['Total (USD)'].sum().sort_values(ascending = False)
print("\n===== Revenue by Customer =====")
print(revenue_by_customer.head(10))

# order quantity by customer
order_quantity_by_customer = sales_data.groupby('Customer Name')['Order Quantity'].sum().sort_values(ascending = False)
print("\n===== Order Quantity by Customer =====")
print(order_quantity_by_customer.head(10))

# total quantity sold
total_quantity_sold = sales_data['Order Quantity'].sum()
print("\n===== Total Quantity Sold =====")
print(total_quantity_sold)

# total tax collected
total_tax_collected = sales_data['Tax (USD)'].sum()
print("\n===== Total Tax Collected =====")
print(total_tax_collected)

# Date Conversion
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Ship Date'] = pd.to_datetime(sales_data['Ship Date'])

# Charts and visualizations
# daily sales data
daily_sales = sales_data.groupby('Order Date')['Total (USD)'].sum().reset_index()
print("\n===== Daily Sales Data =====")
print(daily_sales.head(10))

# Daily sales trend line chart

# create charts folder
os.makedirs('charts', exist_ok=True)

plt.figure(figsize = (12,6))
plt.plot(daily_sales['Order Date'], daily_sales['Total (USD)'], marker = 'o')

# Chart title and labels
plt.title('Daily Sales Trend', fontsize = 16)
plt.xlabel('Order Date', fontsize = 12)
plt.ylabel('Total Sales (USD)', fontsize = 12)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig('charts/daily_sales_trend.png', dpi = 300, bbox_inches = 'tight')
plt.show()

# Top 10 customer by revenue bar chart
# top 10 customers by total revenue

top_customers = (
    sales_data
    .groupby('Customer Name')['Total (USD)']
    .sum()
    .reset_index()
    .sort_values(
        by='Total (USD)',
        ascending=False
    )
    .head(10)
)

print(top_customers)

# charts

plt.figure(figsize = (12,5))

sns.barplot(
data=top_customer,
x = 'Customer Name',
y = 'Total (USD)'
)
# roate customes name
plt.xticks(rotation = 45)

# Chart title and labels
plt.title('Top 10 Customers by Revenue')
plt.xlabel('Customer Name')
plt.ylabel('Total Revenue (USD)')
# adjust layout
plt.tight_layout()

# save the chart
plt.savefig('charts/top_customers_revenue.png', dpi = 300, bbox_inches = 'tight')
plt.show()

# ORDER QUANTITY DISTRIBUTION HISTOGRAM
plt.figure(figsize = (10,5))
sns.histplot(sales_data['Order Quantity'], bins = 5)
# Chart title and labels
plt.title('Order Quantity Distribution')
plt.xlabel('Order Quantity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('charts/order_quantity_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()

# Revenue Distribution box plot
plt.figure(figsize = (8,5))
sns.boxplot(y = sales_data['Total (USD)'])
# Chart title and labels
plt.title('Revenue Distribution')
plt.ylabel('Total Revenue (USD)')
plt.tight_layout()
plt.savefig('charts/revenue_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()

# ======================================
# SALES CORRELATION HEATMAP
# ======================================

plt.figure(figsize=(10,6))

# create correlation matrix
correlation = sales_data.corr(numeric_only=True)

# create heatmap
sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

# chart title
plt.title('Sales Correlation Heatmap')

# adjust layout
plt.tight_layout()

# save chart
plt.savefig(
    'charts/sales_correlation_heatmap.png',
    dpi=300,
    bbox_inches='tight'
)

# show chart
plt.show()