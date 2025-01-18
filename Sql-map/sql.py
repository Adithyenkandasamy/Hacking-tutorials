import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Create a simple SQLite database with a user table
conn = sqlite3.connect('test.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
conn.commit()

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return "Logged in successfully!"
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    app.run(debug=True)
