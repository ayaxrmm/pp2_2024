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



# Function for pagination
def get_phonebook_with_pagination(limit, offset):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY first_name LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# Usage examples
#create a students
create_new_students()
create_new_students()

# Query data with pagination
pagination_results = get_phonebook_with_pagination(limit=5, offset=1)
print(pagination_results)

