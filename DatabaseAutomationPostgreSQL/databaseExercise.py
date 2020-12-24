import psycopg2

try:
    connection = psycopg2.connect(database="staff", user="sakew", password="adolex94",
                                  host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")
else:
    print("Connection to the database was successful!")
cursor = connection.cursor()

cursor.execute('''create table mystaff.employees
                        (id int primary key not null,
                        first_name varchar(25) not null,
                        last_name varchar(25) not null,
                        department varchar(25) not null,
                        phone varchar(25),
                        address varchar(50),
                        salary int);''')

cursor.execute("insert into mystaff.employees (id, first_name,last_name,department,phone,address,salary) \
               values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
                            (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
                            (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
                            (4, 'Karen', 'Wilson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
                            (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")

# updating a record in the database for example  updating  the department for the row(s)
# where the value on the last_name is Doe.

cursor = connection.cursor()
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")

# Deleting records from a table for example deleting all employees with a salary >50000

cursor = connection.cursor()
cursor.execute("delete from mystaff.employees where salary > 50000;")

# Doing multiple queries on database

cursor.execute("select * from mystaff.employees where salary > 5000;")
cursor.execute("select * from mystaff.employees where last_name like '%Richard%';")
cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

# fetching a limited number of entries from database

cursor.execute("select * from mystaff.employees where salary > 50000;")
cursor.execute("select * from mystaff.employees where last_name like '%Emma%';")
cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

# Fetching all the rows in a query result; return a list

records = cursor.fetchall()

# Fetching the next 2 rows in a query result; returns a list

cursor = cursor.fetchmany(size=2)

# Fetching the next row in a query result; return a tuple; returns None when no more records are available

records = cursor.fetchone()

for record in records:
    print(record)

# Committing and Rolling back database transactions
# Commiting (saving) the changes/transactions performed since last commit()
connection.commit()

# Rolling back (undoing) the changes/transactions performed since the last commit()
connection.rollback()

# closing the database connection after all transactions are done.
connection.close()

