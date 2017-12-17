import mysql.connector
import models.Poll
from datetime import date
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AgoraUS.settings")
def loadpoll(pollid):
    cnx = mysql.connector.connect(user='root', password='recvotes',
                                  host='localhost',
                                  database='votaciones_splc')
    cursor = cnx.cursor()

    query = ("SELECT id, title, description, startDate,endDate FROM poll "
             "WHERE id= ")
    query=query+pollid
    start_date = date(2017, 1, 1)
    end_date = date(2019, 12, 31)

    cursor.execute(query)

    # for (id,title, description) in cursor:
    data =cursor.next()
    print "id: "+str(data[0])
    print "title: "+data[1]
    print "description: "+data[2]
    print "startDate: "+str(data[3])
    print "endDate: "+str(data[4])
    # print("ID:{}\nPoll: {}\nDescription: {}".format(cursor.,title, description))
    # poll = Poll(id=data[0],title=data[1],description=data[2],start_date=data[3],end_date=data[4])
    cursor.close()
    cnx.close()


loadpoll(str(10))