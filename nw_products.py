import pyodbc


class NW_Products:
    def __init__(self):
        # set up the details for login
        self.server = 'xxxxxx'  # the server's ip
        self.database = 'Northwind'
        self.username = 'xx'
        self.password = 'xxxxxxx'

        # connect to the server and check that connection
        self.northwind_db = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.northwind_db.cursor()

        #self.cursor.execute("SELECT * INTO arun FROM Products")

        # x self.rows = self.cursor.execute("SELECT * FROM Products").fetchall()
        # eh self.rows = self.cursor.execute("SELECT * FROM arun").fetchall()
        self.rows = self.__setup_table()

    def __setup_table(self):
        # (inspired to do this)
        try:
            # try and set up the rows if the table exists
            return self.cursor.execute("SELECT * FROM arun").fetchall()
        except:
            # create a new table and copy the data from Products into that
            self.cursor.execute("SELECT * INTO arun FROM Products")
        finally:
            return self.cursor.execute("SELECT * FROM arun").fetchall()
