Problem Statement:
In modern business intelligence (BI) workflows, the effective integration and visualization of sales data is key in making well-informed data-driven decisions. This project solves the issue of extracting, processing, and visualizing sales data from a PostgreSQL database in an interactive Streamlit dashboard. The goal is to gain real-time insights into sales trends and category performance.

Technologies Used
•	Backend
        PostgreSQL: Database for storing sales data.
        SQLAlchemy: ORM for database interactions.
        pandas: Data extraction and transformation.
        Python: Core programming language for data processing.
•	Frontend
        Streamlit: Interactive dashboard for visualization.
        Seaborn & Matplotlib: Data visualization.
•	Version Control & CI/CD
        GitHub: Version control.
        Virtual Environments: venv for dependency isolation.
Challenges:
1.	Module Import Errors
Issue: ModuleNotFoundError: No module named 'visualizations'
Solution: Ensured that each directory (backend, frontend, visualizations) contains an __init__.py file, making it a Python package.
2. Database Connection Warning
Issue: pandas only supports SQLAlchemy connectable...
Solution: Changed raw psycopg2 connection to an SQLAlchemy engine for compatibility.
3. Non-GUI Backend for Matplotlib
Issue: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
Solution: Used st.pyplot(fig) instead of plt.show() to correctly render charts in Streamlit.
4. Dataset Size & Performance
Issue: Fetching large datasets from PostgreSQL slowed down performance.
Solution: Implemented pagination in SQL queries and caching with st.cache_data().

Project Structure:
full-stack-bi-project/
│── backend/
│   ├── __init__.py
│   ├── database.py
│── frontend/
│   ├── __init__.py
│   ├── dashboard.py
│── visualizations/
│   ├── __init__.py
│   ├── charts.py
│── main.py
│── requirements.txt
│── README.md

-----------------------------------------------------------------------------

STEPS TO RUN THIS PROJECT IN YOUR ENV:

1. Make sure you have Python 3.9+ is installed on the system.
2. python -m venv venv
source venv/bin/activate  (to activate virtual environment)
3. Install requirements using "pip install -r requirements.txt"
4. Make sure your PostgreSQL is installed and running. Update the DATABASE_URL in backend/database.py if needed.
5. Run for backend server "uvicorn backend.main:app --reload" 
6. Finally, run "streamlit run frontend/dashboard.py" to see visualization in Streamlit. 


