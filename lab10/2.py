import psycopg2

# Connect to the SQLite database
conn = psycopg2.connect(
    host="localhost",
    database="students",
    user="postgres",
    password="Ayau2006"
)

cursor = conn.cursor()

cursor.execute('DROP TABLE user')
conn.commit()
# Create user table if not exists
cursor.execute("""CREATE TABLE user(
            id INT PRIMARY KEY,
            username VARCHAR(255)
);
""")
conn.commit()

# Create user_score table if not exists
cursor.execute('''CREATE TABLE user_score (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    score INTEGER,
                    level INTEGER,
                    FOREIGN KEY (user_id) REFERENCES user(id)
                );
               ''')

# Function to check if a user exists
def check_user_exists(username):
    cursor.execute("SELECT id FROM user WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        return None

# Function to create a new user
def create_user(username):
    cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
    conn.commit()
    return cursor.lastrowid

# Function to get user's current level
def get_user_level(user_id):
    cursor.execute("SELECT level FROM user_score WHERE user_id=?", (user_id,))
    level = cursor.fetchone()
    if level:
        return level[0]
    else:
        return None

# Function to update user's score and level
def update_user_score(user_id, score, level):
    cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)", (user_id, score, level))
    conn.commit()

# Main game logic
def start_game():
    username = input("Enter your username: ")
    user_id = check_user_exists(username)
    
    if user_id:
        print(f"Welcome back, {username}!")
        current_level = get_user_level(user_id)
        if current_level:
            print(f"Your current level is {current_level}.")
        else:
            print("No level found for this user.")
    else:
        print(f"Welcome, {username}!")
        user_id = create_user(username)
    
    # Game starts here
    # Implement your game logic here
    # You can use functions like pause_game(), save_game(), etc.
    
    # For example:
    # game_running = True
    # while game_running:
    #     command = input("Enter command (play/pause/save/quit): ")
    #     if command == "play":
    #         play_game()
    #     elif command == "pause":
    #         pause_game()
    #     elif command == "save":
    #         save_game(user_id, score, level)
    #     elif command == "quit":
    #         game_running = False
    #     else:
    #         print("Invalid command. Try again.")

# Close the database connection when done
def close_connection():
    conn.close()

if __name__ == "__main__":
    start_game()
