import mysql.connector
import hashlib

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="secure_auth_db"
    )

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def secure_login(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT id, username, password_hash, role FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return "Invalid credentials"

    if user["password_hash"] == hash_password(password):
        return f"Login successful. Role: {user['role']}"
    return "Invalid credentials"


if __name__ == "__main__":
    print(secure_login("admin", "admin123"))
