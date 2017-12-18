import mysql.connector
from datetime import date
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AgoraUS.settings")

import django
django.setup()
from recuento.models import Poll
from recuento.models import Question
from recuento.models import QuestionOption
from recuento.models import OptionPerVote
from recuento.models import Vote


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
    #Se extrae la informacion a traves del cursor y se almacena en la base de datos Django
    cursor.execute(query)
    data =cursor.next()
    poll = Poll(id=data[0],title=data[1],description=data[2])
    poll.start_date=data[3]
    poll.end_date=data[4]
    poll.save()



    '''
    Selecionamos las pregunta de la poll anterior y las guardamos en la base de datos
    '''
    # Recogemos la poll guardada para usarla mas adelante
    pollSaved = Poll.objects.get(pk=pollid)
    query = ("SELECT id, title, description, optional,multiple,poll_id FROM question "
             "WHERE poll_id= ")
    query = query + pollid
    cursor.execute(query)
    for data in cursor:
        question = Question(id=data[0],title = data[1],description=data[2],optional=data[3],multiple=data[4],poll=pollSaved)
        question.save()


    '''
      Selecionamos las opciones de cada pregunta y las guardamos en la base de datos
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
    for question in questions:
        for question_option in question.questionoption_set.all():
            query = ("SELECT id,question_option_id, vote_id FROM option_per_vote "
                     "WHERE question_option_id= ")
            query+=str(question_option.id)
            cursor.execute(query)
            questions_option_data=[]
            #en este paso guardamos todos los datos en una lista para poder suar el cursor en otra query,
            #  sin perder la información
            for a in  cursor:
                questions_option_data.append(a)

            #ahora pedimos la información para los votos, e creamos un voto para las optionPervote,
            # en caso de que el voto ya haya sido creado antes, solo se extraera de la base de datos django gracias al
            # "get_or_create", tras eso se crea el optionPerVote
            for data in questions_option_data:
                query = ("SELECT id,token,vote_type_id,vote_date FROM vote "
                         "WHERE id= ")
                query+=str(data[2])

                cursor.execute(query)
                vote_data=cursor.next()
                Vote.objects.get_or_create(id=vote_data[0],token=vote_data[1],vote_type=str(vote_data[2]))
                new_vote = Vote.objects.get(pk=vote_data[0])
                optionPerVote=OptionPerVote(id=data[0],question_option=question_option,vote=new_vote)
                optionPerVote.save()

    cursor.close()
    cnx.close()

if 1==0 :
    loadpoll(str(10))
    print "Esto es la prueba de la carga de la poll: 10"
    print "--------------------------  Las polls: --------------------------"
    for a in Poll.objects.all():
        print str(a.id) + ","+ a.title
    print "-------------------------- Las Questions: -------------------------- "
    for a in Question.objects.all():
        print str(a.id)+ ","+ a.title
    print "-------------------------- Las QuestionOptions: --------------------------"
    for a in QuestionOption.objects.all():
        print str(a.id)+ ","+ a.description
        print "-------------------------- Las OptionPerVotes: -------------------------- "
    for a in OptionPerVote.objects.all():
        print str(a.id)
    print "-------------------------- Los Votes: --------------------------"
    for a in Vote.objects.all():
        print str(a.id)+ ","+ a.token