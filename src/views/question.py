import json
import connection_factory
from bson.objectid import ObjectId
from pyramid.view import view_config
from pyramid.response import Response
from utils import base_layout


@view_config(renderer="../templates/questions.pt", name='question')
def show_question(request):
	question_id = request.GET['id']
	db = connection_factory.create()
	question = db.questions.find_one({'_id': ObjectId(question_id)})
	answers = db.answers.find({'question_id': ObjectId(question_id)}).sort('votes', -1)
	return {'layout': base_layout(), 'question': question, 'answers' : answers}

@view_config(name='answer')
def answer_question(request):
	db = connection_factory.create()
	question_id = request.POST['question_id']
	answer = request.POST['answer']
	db.answers.insert({'answer': answer, 'votes': 0, 'question_id': ObjectId(question_id)})
	return Response()

@view_config(name='upvote_answer')
def upvote_answer(request):
	db = connection_factory.create()
	answer_id = request.POST['answer_id']
	answer = db.answers.find_one({'_id': ObjectId(answer_id)})
	answer['votes'] += 1
	db.answers.save(answer)
	return Response(body=json.dumps({'votes': answer['votes']}))