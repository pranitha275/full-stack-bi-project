from sqlalchemy import create_engine
import pandas as pd

# Define Database URL
DATABASE_URL = "postgresql://postgres:root@localhost:5432/bi_db"

# Function to fetch data using SQLAlchemy
def fetch_sales_data():
    engine = create_engine(DATABASE_URL)  # SQLAlchemy engine
    query = "SELECT date, sales_amount, category FROM sales_data"
    df = pd.read_sql(query, engine)  # Now using SQLAlchemy
    engine.dispose()  # Close connection
    return df
