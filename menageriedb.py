import MySQLdb as mc

# Connect to the MySQL database
conn = mc.connect(host='localhost', user='root', password='1111', database='menagerie')
c = conn.cursor()

#Show all databases
c.execute('SHOW DATABASES;')

databases = c.fetchall()
for db in databases:
    print(db)

# Drop menagerie database if it already exists on systema
c.execute(""" DROP DATABASE IF EXISTS menagerie; """)

# Show Structure of pet table
c.execute("DESCRIBE pet;")
for row in c.fetchall():
    print(row)

# Show all the data in the pet table
c.execute("SELECT * FROM pet;")
for row in c.fetchall():
    print(row)

# Selecting only the data that mentions a femail dog
c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
for row in c.fetchall():
    print(row)

#Selecting only the name and birth columns
c.execute("SELECT name, birth FROM pet;")
for row in c.fetchall():
    print(row)

#Showing the amount of pets each owner has
c.execute("SELECT owner, COUNT(*) as num_pets FROM pet GROUP BY owner ;")
for row in c.fetchall():
    print(row)
    
# SQL query to select name, birth, and the month of birth
c.execute(""" SELECT name, birth, MONTH(birth) FROM pet; """)
conn.commit()

# Fetch all the results
rows = c.fetchall()

# Print the results in a tabular format
print(f"{'name':<10}{'birth':<15}{'MONTH(birth)'}")
for row in rows:
    # Format the birthdate to display as YYYY-MM-DD
    birth_date = row[1].strftime('%Y-%m-%d') if row[1] else "NULL"
    print(f"{row[0]:<10}{birth_date:<15}{row[2]}")

# Close the connection
c.close()
conn.close()
