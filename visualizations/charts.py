import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from backend.database import fetch_sales_data

def plot_sales():
    df = fetch_sales_data()
    if df.empty:
        st.warning("⚠️ No data available to plot.")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="date", y="sales_amount", hue="category", data=df, marker="o", ax=ax)
    ax.set_title("📈 Sales Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales Amount")
    ax.set_xticklabels(df["date"], rotation=45)
    ax.grid(True)

    st.pyplot(fig)  # ✅ Display in Streamlit

def plot_sales_by_category():
    df = fetch_sales_data()
    if df.empty:
        st.warning("⚠️ No data available to plot.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="category", y="sales_amount", data=df, ax=ax)
    ax.set_title("📊 Sales by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales Amount")
    ax.set_xticklabels(df["category"], rotation=45)

    st.pyplot(fig)  # ✅ Display in Streamlit

def plot_sales_pie():
    df = fetch_sales_data()
    if df.empty:
        st.warning("⚠️ No data available to plot.")
        return

    category_sales = df.groupby("category")["sales_amount"].sum()

    fig, ax = plt.subplots(figsize=(7, 7))
    category_sales.plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_title("📊 Sales Distribution by Category")
    ax.set_ylabel("")

    st.pyplot(fig)  # ✅ Display in Streamlit
