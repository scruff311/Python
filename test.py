#name = "Kevin"
#
#if name == "Kevin":
#    print "Hello,", name
#else:
#    print "Oh, well what is your name then?"

#def checkName(name):
#    answer = raw_input("Is your name " + name + "? ")
#
#    if answer.lower() == "yes":
#        print "Hello,", name
#    else:
#        name = raw_input("We're sorry about that. What is your name again? ")
#        print "Welcome,", name
#
#checkName("Kevin")

import MySQLdb

# Setup MySQL Connection
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="python")
cursor = db.cursor()

# Insert a row into our table
cursor.execute("INSERT INTO users (firstname) VALUES ('Kevin')")

# Save changes to database
db.commit()