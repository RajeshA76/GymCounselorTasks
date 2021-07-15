import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

#Creating Department Table
# c.execute("""CREATE TABLE Department (
# 				ID integer,
# 				NAME text,
# 				COMPANY_CODE text,
# 				TOTAL_EMPLOYEES integer)
# 				""")

#Creating Company Table
# c.execute("""CREATE TABLE Company (
# 				CODE text,
# 				NAME text,
# 				COUNTRY text,
# 				TOTAL_EMPLOYEES integer)
# 				""")

#Inserting data into the Department Table
# c.execute("""INSERT INTO Department VALUES
# 			(1,"Engineering & Technology","A101",100),
# 			(2,"Sales,Service & Support","B102",110),
# 			(3,"Marketing & Communications","C103",120),
# 			(4,"Business Strategy","D104",130),
# 			(5,"Marketing & Communications","E105",140);""")

#Inserting data into the Company Table
# c.execute("""INSERT INTO Company VALUES
# 			("A101","GOOGLE","India",500),
# 			("B102","MICROSOFT","Australia",1000),
# 			("C103","GOOGLE","India",250),
# 			("D104","MICROSOFT","Australia",600),
# 			("E105","KPMG","Netherlands",100);""")

c.execute("SELECT SUM(Department.TOTAL_EMPLOYEES) FROM Department JOIN Company ON Department.COMPANY_CODE=Company.CODE WHERE COUNTRY='India';")

result = c.fetchone()

print(f"The sum of the Employees of all Department where the Country is 'India’ is {result[0]}")

conn.commit()

conn.close()