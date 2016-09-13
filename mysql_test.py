import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "WaygoSurveys")
cur = db.cursor()

query = "SELECT * FROM survey6_ios"
cur.execute(query)

data = cur.fetchall()
print(data)