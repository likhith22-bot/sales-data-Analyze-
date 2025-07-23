import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Sample Data:")
print(df.head())

sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_by_product)

sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)

sales_by_product.plot(kind="bar", title="Total Sales by Product", ylabel="Sales", xlabel="Product", color="skyblue")
plt.tight_layout()
plt.show()

sales_by_region.plot(kind="bar", title="Total Sales by Region", ylabel="Sales", xlabel="Region", color="orange")
