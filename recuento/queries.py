import mysql.connector
from datetime import date

def test():

    cnx = mysql.connector.connect(user='root', password='recvotes',
                              host='mysql',
                              database='votaciones_splc')
    cursor = cnx.cursor()

    query = ("SELECT title, description FROM poll "
            "WHERE startDate BETWEEN %s AND %s")

    start_date = date(2017, 1, 1)
    end_date = date(2019, 12, 31)

    cursor.execute(query, (start_date, end_date))

    for (title, description) in cursor:
        print("Poll: {}\nDescription: {}".format(
            title, description))

    cursor.close()
    cnx.close()
    
test()