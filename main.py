from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    
    # df = pd.read_excel(file.file)

    # top_city = df.loc[df["revenue"].idxmax()]["city"]
    # total_revenue = df["revenue"].sum()

    # return {
    #     "top_city": top_city,
    #     "total_revenue": int(total_revenue)
    # }
    df = pd.read_excel(file.file)

    top_city = df.loc[df["revenue"].idxmax()]["city"]
    total_revenue = df["revenue"].sum()
    avg_orders = df["orders"].mean()
    highest_city = df.loc[df["revenue"].idxmax()]["city"]
    lowest_city = df.loc[df["revenue"].idxmin()]["city"]
    avg_revenue = df["revenue"].mean()
    total_orders = df["orders"].sum()
    best_orders_city = df.loc[df["orders"].idxmax()]["city"]

    insights = []

    insights.append(f"{highest_city} generated the highest revenue.")
    insights.append(f"{lowest_city} needs marketing attention.")
    insights.append(f"{best_orders_city} has the strongest customer demand.")
    insights.append(f"{top_city} is the highest performing city.")

    if avg_orders > 130:
        insights.append("Overall demand is strong across cities.")
    else:
        insights.append("Demand is moderate, growth opportunities exist.")

    return {
    "top_city": top_city,
    "total_revenue": int(total_revenue),
    "average_revenue": float(avg_revenue),
    "total_orders": int(total_orders),
    "highest_revenue_city": highest_city,
    "lowest_revenue_city": lowest_city,
    "best_orders_city": best_orders_city,
    "insights": insights
}