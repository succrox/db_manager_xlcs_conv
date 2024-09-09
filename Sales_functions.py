import os
import mysql.connector
from mysql.connector import Error

def insert_sales_in_bulk(df, table_name='students'):
    connection = None
    cursor = None

    try:
        
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv(""),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = f"""
            INSERT INTO {table_name} (code, full_name, emails, course_id)
            VALUES (%s, %s, %s, %s)
            """

            students_data = df.to_records(index=False).tolist()

            cursor.executemany(insert_query, students_data)
            
            connection.commit()

            print(f"{cursor.rowcount} rows inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def get_all_the_courses():
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
                SELECT c.id, c.name FROM courses as c;
            """
            cursor.execute(query)
            courses = cursor.fetchall()
            print(courses)
        except Error as e:
            print(f"Error while getting courses from database: {e}")
        finally:
            cursor.close()
            return courses