import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your_password"
)
mycursor = mydb.cursor()
class TaskList:
    def _init_(self,name,status):
        self.name=name
        self.status=status
    def _str_(self):
        return f'{self.name},{self.status}'

class TaskManager:
    def createdb():
        try:
            mycursor.execute("CREATE DATABASE MyDB")
        except Exception:
            print('Already Created DB')

    def useDB():
        try:
            mycursor.execute("USE MyDB")
        except Exception:
            print('Already Used DB')

    def createProgram():
        try:
            mycursor.execute("CREATE TABLE MyTable (name varchar(100),status varchar(20))")
        except Exception:
            print('Already Created Table')

    def insertProgram():
        try:
            mycursor.execute("INSERT INTO MyTable(name,status) values('breakfast','Completed')")
            mydb.commit()
            print('Inserted Successfully!')
        except Exception:
            print('Already Inserted Data into Table')
    def updateProgram():
        try:
            mycursor.execute("UPDATE MyTable set status='Completed' where name='Coding' ")
            mydb.commit()
            print('Updated Successfully!')
        except Exception:
            print('Already Inserted Data into Table')
    def deleteProgram():
        try:
            mycursor.execute("delete from MyTable  where name='Coding' ")
            mydb.commit()
            print('Deleted Successfully!')
        except Exception:
            print('Issue while Deleting')
tm=TaskManager
#tm.createdb()
tm.useDB()
#tm.createProgram()
tm.insertProgram()
tm.updateProgram()
