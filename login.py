import os
import mysql.connector as sql
from tkinter import *
from tkinter import messagebox


mysql_passcode=os.environ.get('Mysql_passcode') # the environmental variable - 'Mysql_passcode' stores the passcode
# database must also be variablised
mycon=sql.connect(host='localhost',user='root',passwd=mysql_passcode,database='librarymanagement')
cursor_mysql=mycon.cursor()

def login(reg_email_id_login,reg_password_login):

	query_login="select emailid,password from testlogin;"
	cursor_mysql.execute(query_login)
	out=cursor_mysql.fetchall()
	count=0
	for tup in out:
		if tup[0]==reg_email_id_login:   # note : count of each email id in a table is 1 because it is a primary key and google does not accept different email ids   so no needto check for duplicates.
			if tup[1]==reg_password_login:
				retvalue='success'
				bool_val=True
				return bool_val,retvalue
				break
				#break and go to next page

			else:
				retvalue='password incorrect'
				bool_val=False
				return bool_val,retvalue
				break
				#break and reload page by while loop in main program
		else:
			continue
	else:
		if count==0: #count=0 is a false condition because there is 3 cases i)emailfound,passkey correct then program brakes and goes to next page  ii)email found passcode incorrect terminates the loop (does not read the else of for-else) and refreshes page iii)email not found so count is 0 and unnaffected so it displays emailnot found and automatically comes out of the loop (using for-else) and when page is refreshed using while loop.
			retvalue='Registered email id not found'
			bool_val=False
			return bool_val,retvalue