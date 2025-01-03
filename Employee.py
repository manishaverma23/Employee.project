import psycopg2

#Database Connection 

DB_CONFIG = {
    "dbname":"employee_db",
    "user":"postgres",
    "password":"password",
    "host":"localhost",
    "port":5432
}

def connect_db():
    """Connect to the PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connection Successful")
        return conn
    except Exception as e:
        print("Error connecting to database",e)
        return None

# connect_db()