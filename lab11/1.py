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

#delete table
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

# Function to return records based on a pattern
def search_phonebook_pattern(pattern):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    cur.close()
    conn.close()
    
# Function to delete data from the table
def delete_data(filter_type, filter_value, cur, conn):
    if filter_type == 'first_name':
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cur.execute("DELETE FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    conn.commit()
    print("Data deleted successfully.")

# delete_data('phone', '1234567890', cur, conn)


# Usage examples
#create a students
# create_new_students()
# create_new_students()
# Search records based on a pattern
pattern_results = search_phonebook_pattern('Ayau')
print(pattern_results)
if pattern_results == False:
    conn = connect_to_database()
    cur = conn.cursor()
    # cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    delete_data('first_name', '%s', cur, conn)
