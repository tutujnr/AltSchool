# Secure Authentication Module (MySQL)

## Description
This project demonstrates a secure login implementation that is immune to
SQL Injection attacks, replacing the vulnerable logic found in DVWA (Medium).

## Requirements
- Python 3.x
- MySQL 9.x
- mysql-connector-python

## Setup
1. Import `setup_db.sql` into MySQL
2. Edit `secure_auth.py` and set your MySQL password
3. Install dependency:
   pip install mysql-connector-python

## Run Tests
python test.py

## Security Features
- Prepared statements (parameterized queries)
- No dynamic SQL construction
- Passwords hashed using SHA-256
- Resistant to classic SQL injection payloads

## Example SQLi Payload Tested
' OR 1=1 --
(Result: Authentication fails)