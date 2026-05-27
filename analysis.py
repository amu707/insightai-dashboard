# import pandas as pd

# # sample data
# data = {
#     "city": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"],
#     "revenue": [50000, 70000, 65000, 45000, 52000],
#     "orders": [120, 150, 140, 110, 130]
# }

# df = pd.DataFrame(data)

# print("Dataset:")
# print(df)

# # top cities by revenue
# top = df.sort_values(by="revenue", ascending=False)

# print("\nTop cities by revenue:")
# print(top)

# # total revenue
# print("\nTotal revenue:", df["revenue"].sum())


import pandas as pd 
# load excel file
df = pd.read_excel("sales.xlsx")

print("Dataset")
print(df)

top = df.sort_values(by="revenue", ascending=False).head(3)
print("\nTop 3 Cities by Revenue:")
print(top)

total_revenue = df["revenue"].sum()
avg_orders = df["orders"].mean()

print("\nTotal Revenue:", total_revenue)
print("Average Orders:", avg_orders)

best_city = df.loc[df["revenue"].idxmax()]
print("\nInsights:")
print(f"{best_city['city']}is the highest perfoming city.")

if avg_orders > 130:
    print("Overall demand is strong across cities.")
else:
    print("demand is moderate, growth opportunities exist.")
    