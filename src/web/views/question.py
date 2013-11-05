import json
from pyramid.view import view_config
from pyramid.response import Response
from utils import base_layout
from core import question_svc


@view_config(renderer="../templates/questions.pt", name='question')
def show_question(request):
	question_id = request.GET['id']
	question = question_svc.get_question(question_id)
	answers = question_svc.get_question_answers(question_id)	
	return {'layout': base_layout(), 'question': question, 'answers' : answers}


@view_config(name='answer')
def answer_question(request):
	question_id = request.POST['question_id']
	answer = request.POST['answer']
	question_svc.save_answer(question_id, answer)
	return Response()


@view_config(name='vote_answer')
def vote_answer(request):
	answer_id = request.POST['answer_id']
	vote_type = request.POST['vote_type']
	votes = question_svc.vote(answer_id, vote_type)
	return Response(body=json.dumps({'votes': votes}))