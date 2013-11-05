from pyramid.view import view_config
from utils import base_layout
from core import forum_svc, question_svc


@view_config(renderer="../templates/home.pt")
def index(request):
	questions = forum_svc.get_questions()
	return {"questions": questions,
	 		"layout": base_layout(),
	 		"search": False,
	 		"num_found": questions.count()}


@view_config(renderer="../templates/home.pt", name='search')
def search(request):
	search_term = request.GET['search']
	questions = forum_svc.search(search_term)
	return {"questions": questions,
			"layout": base_layout(),
			"search": True,
			"num_found": questions.count()}
	