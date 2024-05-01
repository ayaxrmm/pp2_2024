import psycopg2
import csv
filename = 'phonebook_data.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

conn = psycopg2.connect(
    host="localhost",
    database="students",
    user="postgres",
    password="Ayau2006"
)

cur = conn.cursor()  

#delete table
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
first_name = input("enter first name: ")
last_name = input("enter last name: ")
phone = input("enter phone number: ")
cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
conn.commit()

#update students
cur.execute("""UPDATE phonebook
            SET first_name = 'Ayaulym'
""")
conn.commit()

# Function to query data from the table
def query_data(filter_type, filter_value, cur):
    if filter_type == 'first_name':
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cur.execute("SELECT * FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    result = cur.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("No matching records found.")

query_data('first_name', 'raim', cur)

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

delete_data('phone', '1234567890', cur, conn)
