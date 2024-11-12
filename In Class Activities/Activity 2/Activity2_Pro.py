# DeWayne Rotenberry
# 9/24/2024
# Activity 2 Pro

import DBConnector

def CreateTheTable(my_db):
    """
    This method creates the table we need for this activity
    :return: N/A
    """

    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Rotenberry_DeWayne_Table (MID  VARCHAR, MName  VARCHAR);'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def DropTheTable(my_db):
    """
    This method drops the table we need created for this activity
    :return: N/A
    """

    # SQL command to create a new table
    sqlCommand = 'DROP TABLE Rotenberry_DeWayne_Table;'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def main():
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    CreateTheTable(my_db)
    sqlStatement = 'INSERT INTO Rotenberry_DeWayne_Table VALUES(%s,%s);'
    my_db.query(sqlStatement,('1','One'))
    my_db.query(sqlStatement, ('2', 'Two'))
    my_db.query(sqlStatement, ('3', 'Three'))
    my_db.query(sqlStatement, ('4', 'Four'))
    my_db.query(sqlStatement, ('5', 'Five'))


    DropTheTable(my_db)


if __name__ == "__main__":
    main()