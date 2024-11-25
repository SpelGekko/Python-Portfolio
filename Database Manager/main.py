## Made by Gekko

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    print(f"Connected to database: {db_name}")
    return conn

# Create a table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                genre TEXT,
                release_year INTEGER,
                rating REAL
            )
        ''')
        conn.commit()
        print("Table 'movies' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Insert a record
def insert_record(conn, title, genre, release_year, rating):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movies (title, genre, release_year, rating)
            VALUES (?, ?, ?, ?)
        ''', (title, genre, release_year, rating))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Read records
def read_records(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        records = cursor.fetchall()
        print("Records:")
        for record in records:
            print(record)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Update a record
def update_record(conn, movie_id, title, genre, release_year, rating):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE movies
            SET title = ?, genre = ?, release_year = ?, rating = ?
            WHERE id = ?
        ''', (title, genre, release_year, rating, movie_id))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Delete a record
def delete_record(conn, movie_id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    db_name = 'movies.db'
    conn = connect_db(db_name)
    create_table(conn)

    # Example usage
    insert_record(conn, 'Inception', 'Sci-Fi', 2010, 8.8)
    insert_record(conn, 'The Matrix', 'Sci-Fi', 1999, 8.7)
    read_records(conn)
    update_record(conn, 1, 'Inception', 'Sci-Fi', 2010, 9.0)
    read_records(conn)
    delete_record(conn, 2)
    read_records(conn)
    
    # You can add your commands here to interact with the database. Use the example functions above as a reference.

    conn.close()

if __name__ == "__main__":
    main()