from recuento.models import Poll
from recuento.models import Result
def approvecount(pollid):
    pass
    '''
    Obtener la lista de preguntas de la poll
    '''
    obj = Poll.objects.get(pk=pollid)
    '''
    Por cada pregunta obtener la lista de opciones de la pregunta
    '''

    for question in obj.question_set.all():
        '''
        #   Por cada opcion de la pregunta miramos la longitud del set_optionPerVote->Numero de veces que se ha votado esa opcion
        '''
        QuestionOption=question.questionoption_set.all()
        for option in QuestionOption:
           new_result = Result.object.get_or_create(question_option =option,quantity=len(option.optionpervote_set.all))