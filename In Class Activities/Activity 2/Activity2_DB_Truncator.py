# DeWayne Rotenberry
# CYBY493A_Fall24
# 9/24/24

import DBConnector

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'DROP TABLE Rotenberry_DeWayne_Table;'

# Execute the SQL command.
my_db.query(sqlCommand, '')