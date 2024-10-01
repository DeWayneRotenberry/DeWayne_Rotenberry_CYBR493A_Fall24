# DeWayne Rotenberry
# CYBR493A
# Fall 2024

# Package to connect to DBConnecter, os, time
import DBConnector
import os
from datetime import datetime


print("DeWayne Rotenberry, CYBR493A_Fall24, Homework #1")

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'CREATE TABLE IF NOT EXISTS Rotenberry_DeWayne_HW1_Ips (IP  VARCHAR, TIMESTAMP  VARCHAR, STATUS VARCHAR);'

# Execute the SQL command.
my_db.query(sqlCommand, '')

# 10 random ips
ips = ['192.168.1.1','127.0.0.1']



def ping_something(ip):
     ping_command = f"ping -c 1 {ip}"
     ping_result = os.system(ping_command)
     return ping_result

def main():

    # Main function to prompt for an IP address and check if the host is responding.

    result_from_method = ping_something("")
    print(result_from_method)

for ip in ips:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M") # current timestamp
    status = ping_something(ip) #ping ip get status

# SQL command to insert the result into the database used ChatGPT kept getting error here
    insert_command = f'''
    INSERT INTO Rotenberry_DeWayne_HW1_Ips (IP, TIMESTAMP, STATUS) 
    VALUES ('{ip}', '{current_time}', '{status}');
    '''

    # Execute the insert command
    my_db.query(insert_command, '')

if __name__ == "__main__":
    main()