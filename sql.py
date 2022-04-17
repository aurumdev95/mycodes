import sqlite3

com = sqlite3.connect("employe.db")
c = com.cursor()

#c.execute("""CREATE TABLE employees (
#first text,
#last text,
#pay integer
#)""")
#c.execute('INSERT INTO employees VALUES ("corey", "schafler", 5000)')

c.execute("SELECT * FROM employees WHERE last='schafler'")

print(c.fetchone())

#c.fetchmany()
#c.fetchall()

com.commit()


com.close()