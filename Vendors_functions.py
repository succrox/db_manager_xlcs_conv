import os
import mysql.connector
from mysql.connector import Error
import streamlit as st
import pandas as pd

def insert_vendors_in_bulk(df):
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
            INSERT INTO vendors (Nombre, Zona, Telefono, Correo, Meta, Ventas, Comisiones, Clientes, Estado, Comentarios)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

def get_all_the_vendors():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password="",
        database=os.getenv("DB_NAME")
    )

    vendors = []

    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT v.ID, v.Nombre FROM vendors as v;
            """
            cursor.execute(query)
            vendors = cursor.fetchall()
        except Error as e:
            print(f"Error while getting vendors from database: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()
            return(vendors)
        
def insert_single_vendor(values):
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password="",
        database=os.getenv("DB_NAME")
    )
    try:
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = """
            INSERT INTO vendors (Nombre, Zona, Telefono, Correo, Meta, Ventas, Comisiones, Clientes, Estado, Comentarios)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

def extract_vendors_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

    df = df.rename(columns={
        'Nombre Completo': 'name',
        'Zona de Ventas': 'zone',
        'Teléfono': 'phone',
        'Correo Electrónico': 'mail',
        'Meta de Ventas Mensual': 'goal',
        'Ventas Realizadas': 'sales',
        'Comisiones': 'comm',
        'Clientes Asignados': 'client',
        'Estado': 'state',
        'Comentarios': 'desc'
    })
    
    return(df)
