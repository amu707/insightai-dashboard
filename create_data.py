import pandas as pd
data = {
    "city": ["mumbai","delhi","banglore", "chennai","hyderabad"],
    "revenue": [50000, 70000, 65000, 45000, 52000],
    "orders": [120, 150,140,110,130]  
}
df = pd.DataFrame(data)
df.to_excel("sales.xlsx", index = False)
print("sales.xlsx created successfully!")
