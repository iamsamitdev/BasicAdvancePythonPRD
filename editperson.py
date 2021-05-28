import pymysql
from dbpackage import ConnectMySQL as con


def edit_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
         UPDATE person SET 
         fullname='somkid',
         weight='55',
         height='158' 
         WHERE id='2'
        """
    try:
        cursor.execute(sql)
        connection.commit()
        print('Update person success.')
    except pymysql.err:
        print(pymysql.err)


edit_person()
