import os
import psycopg2
import logging
from flask import Flask, request, render_template

# Configure logging
#logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

app = Flask(__name__)

# Use environment variables to configure the database connection
DATABASE_URL = (
    f"dbname='{os.getenv('DB_NAME')}' "
    f"user='{os.getenv('DB_USER')}' "
    f"password='{os.getenv('DB_PASSWORD')}' "
    f"host='{os.getenv('DB_HOST')}'"
)

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# SQL command to create a table named "users" in the "test" schema
# create_table_sql = """
# CREATE TABLE IF NOT EXISTS test.users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(255),
#     email VARCHAR(255)
# );
# """

# # Establish a connection to the database
# conn = get_db_connection()
# cur = conn.cursor()
# # Execute the SQL command to create the table
# cur.execute(create_table_sql)
# cur.close()
# conn.close()

@app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    conn = get_db_connection()
    username = request.form['username']
    email = request.form['email']
    conn.execute("INSERT INTO test.users (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()
    conn.close()
    return "Submitted!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
