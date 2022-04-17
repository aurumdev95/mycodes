import sqlite3
from scr import Employee

com = sqlite3.connect("employe.db")
c = com.cursor()
#c.execute("""CREATE TABLE employees (
#first text,
#last text,
#pay integer
#)""")
def insert(emp):
	with com:
		c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first": emp.first, "last": emp.last, "pay": emp.pay})
	
	
	

def getemp(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
	return c.fetchall()
	
def update_pay(emp, pay):
	with com:
		c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {"first": emp.first, "last": emp.last, "pay": pay})
	
def remove(emp):
	with com:
		c.execute("DELETE from employees WHERE first = :first AND last = :last", {"first": emp.first, "last": emp.last})
#	
#emp1 = Employee("eric", "johnson", 50000)
#emp2 = Employee("eric", "patric", 38388)

#insert(emp1)
#insert(emp2)

#print(getemp("patric"))
#update_pay(emp2, 83883883)
#print(getemp("patric"))

remove(emp2)




com.close()