import connection_factory
import json
from pyramid.view import view_config
from pyramid.renderers import get_renderer
from pyramid.httpexceptions import HTTPFound
from bson.objectid import ObjectId


def base_layout():
    renderer = get_renderer("../templates/base.pt")
    layout = renderer.implementation().macros['layout']
    return layout


@view_config(renderer="../templates/home.pt")
def index(request):
	db = connection_factory.create()
	questions = db.questions.find()
	return {"questions": questions, "layout": base_layout()}


@view_config(renderer="../templates/ask.pt", name='ask')
def ask(request):
    return {"layout": base_layout()}


@view_config(name='save_question')
def save_question(request):
	db = connection_factory.create()
	params_dict = request.params.mixed()
	params_dict['tags'] = params_dict['tags'].split(',')
	params_dict['answers'] = []
	question_id = db.questions.insert(params_dict)
	red = 'question?id=%s' % question_id
	return HTTPFound(location=red)


@view_config(renderer="../templates/questions.pt", name='question')
def show_question(request):
	question_id = request.GET['id']
	db = connection_factory.create()
	question = db.questions.find_one({'_id': ObjectId(question_id)})
	return {'layout': base_layout(), 'question': question}

@view_config(renderer="../templates/home.pt", name='search_question')
def search_question(request):
	db = connection_factory.create()
	search_term = request.GET['search']
	questions = db.questions.find({'tags': search_term})
	return {"questions": questions, "layout": base_layout()}