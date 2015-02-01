from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

##### in this script, i add a resident to 
cnx = mysql.connector.connect(host= "localhost", user = "root", passwd = "l3nny", database = "bewohner")

cursor = cnx.cursor()

###TABLES['employees'] = (
###    "CREATE TABLE `employees` ("
###    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
###        "  `birth_date` date NOT NULL,"
###    "  `first_name` varchar(14) NOT NULL,"
###    "  `last_name` varchar(16) NOT NULL,"
###    "  `gender` enum('M','F') NOT NULL,"
###        "  `hire_date` date NOT NULL,"
###    "  PRIMARY KEY (`emp_no`)"
###        ") ENGINE=InnoDB")


tomorrow = datetime.now().date() + timedelta(days=1)

add_res = ("INSERT INTO einwohner "
                "(vorname, nachname) "
           "VALUES (%s, %s)")

data_res = ('Wolf', 'Ranzen')

#insert:
cursor.execute(add_res, data_res)

res_no = cursor.lastrowid

cnx.commit()

cursor.close()

