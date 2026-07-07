import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Sales_Data.csv", encoding="utf-8-sig")

# Display first 5 rows
print("First 5 Rows")
print(df.head())

print("\n--------------------------")

# Display dataset information
print("Dataset Information")
print(df.info())

print("\n--------------------------")

# Display dataset statistics
print("Statistical Summary")
print(df.describe())

# First 5 rows
print("\n===== First 5 Rows =====")
print(df.head())

# Last 5 rows
print("\n===== Last 5 Rows =====")
print(df.tail())

# Shape of dataset
print("\n===== Shape =====")
print(df.shape)

# Column names
print("\n===== Columns =====")
print(df.columns)

# Data types
print("\n===== Data Types =====")
print(df.dtypes)
print("\n===== Dataset Info =====")
df.info()
print("\n===== Missing Values =====")
print(df.isnull().sum())
print("\n===== Duplicate Rows =====")
print(df.duplicated().sum())
print("\n===== Statistical Summary =====")
print(df.describe())


# ==========================================
# BUSINESS ANALYSIS
# ==========================================

print("\n========== BUSINESS ANALYSIS ==========\n")
print("Total Sales")
print(df["Sales"].sum())

print("\nTotal Profit")
print(df["Profit"].sum())

print("\nTotal Orders")
print(df["Order ID"].count())

print("\nSales by Region")

sales_region = df.groupby("Region")["Sales"].sum()

print(sales_region)

print("\nProfit by Category")

profit_category = df.groupby("Category")["Profit"].sum()

print(profit_category)

print("\nTop 10 Customers")

top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

print("\nTop 10 Products")

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

print("\nMonthly Sales")

monthly_sales = (
    df.groupby(df["Order Date"].dt.month_name())["Sales"]
    .sum()
)

print(monthly_sales)

print("\nHighest Sale")

print(df["Sales"].max())

print("\nLowest Sale")

print(df["Sales"].min())


 # ==========================================
# DATA VISUALIZATION
# ==========================================

sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("Charts/Sales_by_Region.png")

plt.show()

profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("Charts/Profit_by_Category.png")

plt.show()


monthly_sales = (
    df.groupby(df["Order Date"].dt.month_name())["Sales"]
    .sum()
)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("Charts/Monthly_Sales.png")

plt.show()



top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
top_products.plot(kind="bar")

plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Charts/Top_Products.png")

plt.show()



top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_customers.plot(kind="barh")

plt.title("Top 10 Customers")
plt.xlabel("Sales")
plt.ylabel("Customer")

plt.tight_layout()

plt.savefig("Charts/Top_Customers.png")

plt.show()