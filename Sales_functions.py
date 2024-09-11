import os
import mysql.connector
from mysql.connector import Error
import streamlit as st
import pandas as pd

def insert_sale_in_bulk(df):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password="",
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = f"""
            INSERT INTO sales (Id_vendor, Name_client, Product, Quantity, Unitary_p, Tot_sale, Payment, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            data = df.to_records(index=False).tolist()

            cursor.executemany(insert_query, data)
            
            connection.commit()

            st.write(f"{cursor.rowcount} rows inserted successfully.")

    except Error as e:
        st.write(f"Error: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def get_all_the_sales():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password="",
        database=os.getenv("DB_NAME")
    )

    sales = []

    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT s.ID, s.Id_vendor, s.Product, s.Tot_sale FROM sales as s;
            """
            cursor.execute(query)
            sales = cursor.fetchall()
            print(sales)
        except Error as e:
            print(f"Error while getting sales from database: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()
            return sales
        
def insert_single_sale(values):
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password="",
        database=os.getenv("DB_NAME")
    )
    try:
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = f"""
            INSERT INTO sales (Id_vendor, Name_client, Product, Quantity, Unitary_p, Tot_sale, Payment, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(query, values)
            connection.commit()

            st.write(f"{cursor.rowcount} rows inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def extract_sale_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

    df = df.rename(columns={
        'ID Vendedor': 'vendor',
        'Nombre del Cliente': 'client',
        'Producto': 'product',
        'Cantidad': 'quantity',
        'Precio Unitario': 'unitary',
        'Total de la Venta': 'sale',
        'Método de Pago': 'payment',
        'Estado de la Venta': 'state'
    })
    
    return(df)
