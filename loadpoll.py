import mysql.connector
from datetime import date
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AgoraUS.settings")

import django
django.setup()
from recuento.models import Poll
from recuento.models import Question
from recuento.models import QuestionOption


def loadpoll(pollid):
    cnx = mysql.connector.connect(user='root', password='recvotes',
                                  host='localhost',
                                  database='votaciones_splc')
    cursor = cnx.cursor()
    '''
    Selecionamos la poll y la guardamos en la base de datos
    '''
    query = ("SELECT id, title, description, startDate,endDate FROM poll "
             "WHERE id= ")
    query=query+pollid

    cursor.execute(query)

    data =cursor.next()

    poll = Poll(id=data[0],title=data[1],description=data[2])
    poll.start_date=data[3]
    poll.end_date=data[4]
    poll.save()
    pollSaved = Poll.objects.get(pk=10)
    #print obj.title


    '''
    Selecionamos las pregunta de la poll anterior y las guardamos en la base de datos
    '''
    query = ("SELECT id, title, description, optional,multiple,poll_id FROM question "
             "WHERE poll_id= ")
    query = query + pollid
    cursor.execute(query)
    for data in cursor:
        question = Question(id=data[0],title = data[1],description=data[2],optional=data[3],multiple=data[4],poll=pollSaved)
        question.save()
    pollSaved = Poll.objects.get(pk=10)


    '''
      Selecionamos las opciones de cada preguntay las guardamos en la base de datos
    '''
    questions =  pollSaved.question_set.all()
    for question in questions:
        query = ("SELECT id,description,question_id FROM question_option "
                 "WHERE question_id= ")
        query +=str(question.id)
        cursor.execute(query)
        for data in cursor:
            question_option = QuestionOption(id=data[0],description=data[1],question=question)
            question_option.save()

    '''
    Selecionamos las OptionPerVote de cada opcion de pregunta las guardamos en la base de datos
    '''
    cursor.close()
    cnx.close()


loadpoll(str(10))