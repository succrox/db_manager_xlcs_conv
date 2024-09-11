import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

st.title("Sales by vendor")
def get_data():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password="",
        database=os.getenv("DB_NAME")
    )
    data = []

    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT v.Nombre, s.Name_client, s.Product, s.Tot_sale FROM sales as s INNER JOIN vendors as v ON s.Id_vendor = v.ID;
            """
            cursor.execute(query)
            data = cursor.fetchall()
        except Error as e:
            print(f"Error while getting sales or vendors from database: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()
            return data

data = get_data()

df_table = pd.DataFrame(data)

st.table(df_table)







