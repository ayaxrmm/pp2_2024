import psycopg2

# Function to connect to the database
def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="students",
        user="postgres",
        password="Ayau2006"
    )
    return conn

# #delete table
conn = connect_to_database()
cur = conn.cursor()
cur.execute('DROP TABLE phonebook')
conn.commit()

#create a new table
cur.execute("""CREATE TABLE phonebook(
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone VARCHAR(20)
            );
""")
conn.commit()

#create new students
def create_new_students():
    first_name = input("enter first name: ")
    last_name = input("enter last name: ")
    phone = input("enter phone number: ")
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()


# Procedure to insert new user or update if exists
def insert_or_update_user(first_name, last_name, phone):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM phonebook WHERE first_name = %s)", (first_name,))
    exists = cur.fetchone()[0]
    if exists:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (phone, first_name))
    else:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()


# Usage examples
#create a students
create_new_students()
create_new_students()

# Insert or update a user
insert_or_update_user('akni', 'kuan', '12345')
