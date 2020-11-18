import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="" # Set your username made for SQL database,
  password="", # Set your password made for SQL database
  database="" # Set your own Database name
)

mycursor = mydb.cursor()

def getSqlData():
	try:
		mycursor.execute("SELECT * FROM usercredentials")
		record = mycursor.fetchall()
		for i in record:
			print(i)

		if mycursor.rowcount == 0:
			print("No Data Present")

	except Exception as e:
		print(f"Error: {e}")
		print("Cannot fetch the data")

def deleteSqlData():
	try:
		testQuery = input("Enter sitename: ")
		addr = (testQuery, )
		query = "DELETE FROM usercredentials WHERE sitename = %s"
		mycursor.execute(query, addr)
		# pass
		mydb.commit()
		print("Data successfully got deleted")

	except Exception as e:
		print(f"Error: {e}")
		print("Cannot delete the data")

def setInputSqlData():
	try:
		sitename = input("Website URL(Enter full URL): ")
		username = input("Website Username: ")
		email = input("Enter EMail Address: ")
		password = input("Enter Password: ")

		query = "INSERT INTO usercredentials (sitename, username, email, password) VALUES (%s, %s, %s, %s)"
		val = (sitename, username, email, password)
		mycursor.execute(query, val)
		mydb.commit()

		print("Data got successfully stored")
	except Exception as e:
		print(f'Error: {e}')
		print("Cannot insert data")

# ========================================================================

if __name__ == '__main__':

	commandPallete = ["gdata -> To Get Data", "ddata -> To Delete Data", "idata -> To Insert Data", "quit -> To Close The Application"]
	for i in commandPallete:
		print("Command: ", i)
	print("="*90)

	while True:
		inpCommand = input("Enter Command: ").lower()
		if inpCommand == "gdata".lower():
			getSqlData()

		elif inpCommand == "ddata".lower():
			deleteSqlData()

		elif inpCommand == "idata".lower():
			setInputSqlData()

		elif inpCommand == "quit".lower():
			break
