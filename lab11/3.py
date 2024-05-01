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
# def create_new_students():
#     first_name = input("enter first name: ")
#     last_name = input("enter last name: ")
#     phone = input("enter phone number: ")
#     cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
#     conn.commit()


# Procedure to insert many new users and check correctness of phones
def insert_many_users(users_list):
    conn = connect_to_database()
    cur = conn.cursor()
    incorrect_data = []
    for user in users_list:
        first_name, last_name, phone = user.split(',')
        if len(phone.strip()) != 10:  # Assuming phone number length is 10 digits
            incorrect_data.append((first_name, last_name, phone))
        else:
            cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name.strip(), last_name.strip(), phone.strip()))
    conn.commit()
    cur.close()
    conn.close()
    return incorrect_data



# Usage examples
#create a students
# create_new_students()
# create_new_students()

# Insert many new users
incorrect_data = insert_many_users(['Aya,Raimbek,1234567890', 'Akni,Kuanysh,9876543210', 'Zhuz,Yerniazova,1234567'])
