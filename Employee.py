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

def add_employee(name,position,salary):
    """ Add new employee to database"""
    query= "INSERT INTO emp(name,position,salary) VALUES(%s,%s,%s)"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query,(name,position,salary))
                conn.commit()
                print("Employee added succesfully")
        except Exception as e:
            print(" Error adding employee",e)
        
        finally:
            conn.close()

add_employee('rama','manager',50000)

