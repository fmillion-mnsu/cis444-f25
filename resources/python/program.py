import oracledb
import pymssql  

# BEFORE YOU RUN THE PROGRAM, you must CHANGE this information 
# to match the required information for your SQL Server!
MSSQL_HOST = "your_server.campus-quest.com"
MSSQL_PORT = 1433 # your port here!
MSSQL_USER = "username_goes_here"
MSSQL_PASSWORD = "password_goes_here"
MSSQL_DB = "SP" # you can change this to another DB.

# BEFORE YOU RUN THE PROGRAM, you must COMMENT OUT OR REMOVE
# this line! Only do this after you have updated the above
# lines to point to YOUR database server!
raise SystemError("You did not read the instructions!")

conn_error = False

# Attempts to create a connection to SQL Server.
try:
    conn_mssql = pymssql.connect(server=MSSQL_HOST, user=MSSQL_USER, password=MSSQL_PASSWORD, port=MSSQL_PORT, database=MSSQL_DB)
    print("MSSQL connected OK.")
except Exception as e:
    print(f"Exception connecting to MSSQL: {e}")
    conn_error = True

if conn_error:
    print("There were connection errors. Aborting execution.")
    exit(1)

print("Connection made successfully.")
print()

# Get a cursor for MSSQL
m_cursor = conn_mssql.cursor()

print("MSSQL: select S#, SNAME from S:")
m_cursor.execute("select S#, SNAME from S")
for row in m_cursor.fetchall():
    print(row)
print()
