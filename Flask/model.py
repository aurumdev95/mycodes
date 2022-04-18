import sqlite3
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
	con = sqlite3.connect(path.join(ROOT, "database.db"))
	c = con.cursor()
	c.execute("insert into posts (name, content) values(:name, :content)", {"name": name, "content": content})
	con.commit()
	con.close()
	
def get_post():
	con =  sqlite3.connect(path.join(ROOT, "database.db"))
	c = con.cursor()
	c.execute("select * from posts")
	posts = c.fetchall()
	return posts
	
#con = sqlite3.connect("database.db")
#c = con.cursor()	
#c.execute("""CREATE TABLE posts (
#name text,
#content text 
#)""")
#con.commit()
#con.close()