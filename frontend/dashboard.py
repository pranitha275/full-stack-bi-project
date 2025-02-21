import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import streamlit as st
from visualizations.charts import plot_sales, plot_sales_by_category, plot_sales_pie

st.title("📊 Sales Analytics Dashboard")

if st.button("Show Sales Trend 📈"):
    plot_sales()

if st.button("Show Sales by Category 📊"):
    plot_sales_by_category()

if st.button("Show Sales Distribution 🥧"):
    plot_sales_pie()


