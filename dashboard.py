
from reportlab.pdfgen import canvas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# streamlit run dashboard.py
# st.title("AI Analyst Dashboard")

st.title("InsightAI")
st.caption("AI-Powered Business Intelligence Platform")

st.sidebar.title("InsightAI")
st.sidebar.write("AI Business Intelligence Dashboard")
st.sidebar.markdown("---")
st.sidebar.info(
    "Upload your business data to generate AI-powered insights and reports."
)
st.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "Upload Business Data",
    type=["xlsx", "csv"]
)
if uploaded_file:

   # df = pd.read_excel(uploaded_file)
#    if uploaded_file.name.endswith(".csv"):
#     df = pd.read_csv(uploaded_file)

# else:
#     df = pd.read_excel(uploaded_file)
   
   try:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    required_columns = ["city", "revenue", "orders"]

    for col in required_columns:
        if col not in df.columns:
            st.error(f"Missing column: {col}")
            st.stop()

   except Exception:
    st.error("Please upload a valid CSV or Excel file.")
    st.stop()
# above codes ensures that instead of crashing it'll ask for a valid upload 
   total_revenue = df["revenue"].sum()
   avg_revenue = df["revenue"].mean()

   highest_city = df.loc[df["revenue"].idxmax()]["city"]
   lowest_city = df.loc[df["revenue"].idxmin()]["city"]
   best_orders_city = df.loc[df["orders"].idxmax()]["city"]
   avg_orders = df["orders"].mean()

   st.subheader("Business Metrics")

   col1, col2 = st.columns(2)

   with col1:
    st.metric("Total Revenue", int(total_revenue))
  
   with col2:
    st.metric("Average Revenue", round(avg_revenue, 2))

   col3, col4 = st.columns(2)

   with col3:
    st.metric("Top City", highest_city)

   with col4:
    st.metric("Lowest City", lowest_city)

   col5, col6 = st.columns(2)

   with col5:
    st.metric("Best Orders City", best_orders_city)

   with col6:
    st.metric("Average Orders", round(avg_orders, 2))

   st.subheader("Revenue by City")

   fig, ax = plt.subplots()

   ax.bar(df["city"], df["revenue"])

   st.pyplot(fig)

   st.subheader("Orders by City")

   fig2, ax2 = plt.subplots()

   ax2.plot(df["city"], df["orders"], marker="o")

   st.pyplot(fig2)

   st.subheader("Revenue Share")

   fig3, ax3 = plt.subplots()

   ax3.pie(
    df["revenue"],
    labels=df["city"],
    autopct="%1.1f%%"
   )

   st.pyplot(fig3)

   st.subheader("AI Business Recommendation")

   if highest_city == best_orders_city:
     st.success(f"{highest_city} is your strongest market. Increase marketing investment there.")

   if lowest_city != highest_city:
     st.warning(f"{lowest_city} needs attention. Consider offers or local campaigns.")

   st.subheader("Raw Data")

   st.dataframe(df)
   pdf_file = "business_report.pdf"

   c = canvas.Canvas(pdf_file)

   c.drawString(100, 800, "InsightAI Business Report")

   c.drawString(100, 760, f"Total Revenue: {total_revenue}")

   c.drawString(100, 740, f"Average Revenue: {avg_revenue}")

   c.drawString(100, 720, f"Top City: {highest_city}")

   c.drawString(100, 700, f"Lowest City: {lowest_city}")

   c.save()

   with open(pdf_file, "rb") as file:
     st.download_button(
        label="Download AI Report",
        data=file,
        file_name="InsightAI_Report.pdf",
        mime="application/pdf"
    )
   from io import BytesIO

   pdf_buffer = BytesIO()

   doc = SimpleDocTemplate(pdf_buffer)
   styles = getSampleStyleSheet()

   elements = []

   elements.append(Paragraph("InsightAI Business Report", styles['Title']))
   elements.append(Spacer(1, 12))

   elements.append(Paragraph(f"Total Revenue: {total_revenue}", styles['BodyText']))
   elements.append(Paragraph(f"Average Revenue: {avg_revenue}", styles['BodyText']))
   elements.append(Paragraph(f"Top City: {highest_city}", styles['BodyText']))
   elements.append(Paragraph(f"Lowest City: {lowest_city}", styles['BodyText']))
   elements.append(Paragraph(f"Best Orders City: {best_orders_city}", styles['BodyText']))
   elements.append(Paragraph(f"Average Orders: {avg_orders}", styles['BodyText']))

   doc.build(elements)

   st.download_button(
      label="Download AI Report PDF",
      data=pdf_buffer.getvalue(),
      file_name="InsightAI_Report.pdf",
      mime="application/pdf"
   )