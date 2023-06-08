"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2


def get_filepath(relative_path):
    file_path = os.path.join(base_path, relative_path)
    return file_path


base_path = r'C:\PythonProjects\postgres-homeworks'

conn = psycopg2.connect(host="localhost", database='north', user='postgres', password='0000')
try:
    with conn:
        with conn.cursor() as cur:

            relative_path = r'homework-1\north_data\customers_data.csv'
            file_path = get_filepath(relative_path)
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Пропустить заголовок CSV
                for row in reader:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

            relative_path = r'homework-1\north_data\employees_data.csv'
            file_path = get_filepath(relative_path)
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Пропустить заголовок CSV
                for row in reader:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)

            relative_path = r'homework-1\north_data\orders_data.csv'
            file_path = get_filepath(relative_path)
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Пропустить заголовок CSV
                for row in reader:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)

finally:
    conn.close()
