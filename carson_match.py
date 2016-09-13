import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "python")
cursor = db.cursor()

# get song input from user and check if it is real
valid_song = 0
while valid_song == 0:
	song = raw_input("What song would you like matches for? ").title()
	query = "SELECT * FROM carson_daily WHERE title = '{}'" .format(song)
	cursor.execute(query)
	if cursor.rowcount:
		valid_song = 1
	else:
		print "No songs found."

# get song tuning and matches
query = "SELECT tuning FROM carson_daily WHERE title = '{}'" .format(song)
cursor.execute(query)
row = cursor.fetchone()
tuning = row[0]
print "\nThe tuning of {} is {}. Here are the matches:" .format(song, tuning)
tuning_query = ("SELECT title FROM carson_daily WHERE tuning = '{}' AND title != '{}'"
.format(tuning, song))
cursor.execute(tuning_query)
tuning_results = cursor.fetchall()
for song_array in tuning_results:
	print song_array[0]

# get song starting note and matches
query = "SELECT starting_note FROM carson_daily WHERE title = '{}'" .format(song)
cursor.execute(query)
row = cursor.fetchone()
start = row[0]
print "\nThe starting note of {} is {}. Here are songs that end with a {}:" .format(song, start, start)
starting_query = ("SELECT title FROM carson_daily WHERE ending_note = '{}' AND title != '{}'"
.format(start, song))
cursor.execute(starting_query)
starting_results = cursor.fetchall()
for song_array in starting_results:
	print song_array[0]

# get song ending note and matches
query = "SELECT ending_note FROM carson_daily WHERE title = '{}'" .format(song)
cursor.execute(query)
row = cursor.fetchone()
end = row[0]
print "\nThe ending note of {} is {}. Here are songs that start with a {}:" .format(song, end, end)
ending_query = ("SELECT title FROM carson_daily WHERE starting_note = '{}' AND title != '{}'"
.format(end, song))
cursor.execute(ending_query)
ending_results = cursor.fetchall()
for song_array in ending_results:
	print song_array[0]
print "\n"

# song = raw_input("What song would you like matches for? ").title()
# query = "SELECT * FROM carson_daily WHERE title = '{}'" .format(song)
# cursor.execute(query)
# row = cursor.fetchone()
# if row is None:
#     print "There is no song titled {}" .format(song)
#     exit()

# # ask user which match they are looking for
# match_types = ["tuning", "starting_note", "ending_note"]
# selection_number = 0
# while selection_number not in ('1', '2', '3'):
#     selection_number = raw_input("What match are looking for?\n1: Tuning\n2: Starting\n3: Ending\n")
#     if selection_number not in ('1', '2', '3'):
#         print "\nInvalid selection"

# # grab the parameter that the user would like to match and display
# match_type = match_types[int(selection_number)-1]
# query = "SELECT {} FROM carson_daily WHERE title = '{}'" .format(match_type, song)
# cursor.execute(query)
# row = cursor.fetchone()
# match_parameter = row[0]
# print "\nThe {} of {} is {}" .format(match_type, song, match_parameter)

# # swap starting and ending match parameters since we are looking for the opposite
# if selection_number == '2':
#     match_type = "ending_note"
# elif selection_number == '3':
#     match_type = "starting_note"

# fetch and display results
# query = ("SELECT title, tuning, starting_note, ending_note FROM carson_daily WHERE {} = '{}' AND title != '{}'"
# .format(match_type, match_parameter, song))
# cursor.execute(query)
# results = cursor.fetchall()
# print "Here are songs with a {} of {}" .format(match_type, match_parameter)
# print(results)

#for results in cursor:
#    tuning = results[0]
#    print "The tuning for {} is {}" .format(song, tuning)
#
#print "Again, that is {}" .format(tuning)

#tuning = cursor.fetchall()
#print(tuning)

#row = cursor.fetchone()
#    
#while row is not None:
#    print(row)
#    row = cursor.fetchone()


#if tuning == "E":
#    print "This song is in E"
#else:
#    print "This song is not in E"