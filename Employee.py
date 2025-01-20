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

# add_employee('rama','manager',50000)

def view_employees():
    query="SELECT * FROM emp"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                emp=cursor.fetchall()
                print("\n Employee List")
                for eone in emp:
                    print(f"Id:{eone[0]},name:{eone[1]},position:{eone[2]},salary:{eone[3]}")
        except Exception as e:
            print("Error adding emp",e)
        finally:
            conn.close()
# view_employees()
def update_employee(empid,name=None,position=None,salary=None):
    query="UPDATE emp SET name=COALESCE(%s,name),position=COALESCE(%s,position),salary=COALESCE(%s,salary) WHERE id=%s"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor()as cursor:
                cursor.execute(query,(name,position,salary,empid))
                conn.commit()
                print("Employee added succesfully")
        except Exception as e:
            print("Error Updating",e)
        finally:
            conn.close()
# update_employee(1,"Akki","Manager",300)


def delete_employee(empid):
    query="DELETE FROM emp where id=%s"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query,(empid,))
                conn.commit()
                print("Employee Details Deleted")
        except Exception as e:
            print("Error Deleting Details",e)
        finally:
            conn.close()
# delete_employee(2)

def main():
     """Main Menu For Employe Mangament System"""
     while True:
         print("\n Employe Managment System")
         print("1.Add Employe")
         print("2.View Employee")
         print("3.Update Employee")
         print("4.Delete Employee")
         print("5.Exit")
         
         choice=input("Enter Youe choice:")
         if choice=="1":
             name=input("Enter Name")
             position=input("Enter Position")
             salary=int(input("Enter Salary"))
             add_employee(name,position,salary)
             
         elif choice=="2":
             view_employees()
         elif choice=="3":
             empid=int(input("Enter Id")) or None
             name=input("Enter Name") or None
             position=input("Enter Position") or None
             salary=input("Enter Salary:") or None
             salary=int(salary) if salary else None
             update_employee(empid,name,position,salary)
             
         elif choice=="4":
             empid=int(input("Enter Id:"))
             delete_employee(empid)
             
         elif choice=="5":
             print("System Execueted")
             break
         else:
             print("Invalid choice ")
             
if __name__=="__main__":
    main()
