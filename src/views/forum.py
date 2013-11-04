import connection_factory
from pyramid.view import view_config
from utils import base_layout


@view_config(renderer="../templates/home.pt")
def index(request):
	db = connection_factory.create()
	questions = db.questions.find()
	return {"questions": questions, "layout": base_layout()}


@view_config(renderer="../templates/home.pt", name='search_question')
def search_question(request):
	db = connection_factory.create()
	search_term = request.GET['search']
	questions = db.questions.find({'tags': search_term})
	return {"questions": questions, "layout": base_layout()}
