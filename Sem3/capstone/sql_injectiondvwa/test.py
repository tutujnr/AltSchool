from secure_auth import secure_login

# Valid login
print(secure_login("admin", "admin123"))

# Invalid password
print(secure_login("admin", "wrongpass"))

# SQL Injection attempt
print(secure_login("' OR 1=1 --", "anything"))