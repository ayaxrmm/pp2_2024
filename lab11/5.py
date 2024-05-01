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

# Procedure to delete data by username or phone
def delete_from_phonebook(username=None, phone=None):
    conn = connect_to_database()
    cur = conn.cursor()
    if username:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        raise ValueError("Both username and phone cannot be None.")
    conn.commit()
    cur.close()
    conn.close()

create_new_students()
create_new_students()
create_new_students()

# Delete data by username or phone
delete_from_phonebook(username='Ayau')
delete_from_phonebook(phone='9876543210')