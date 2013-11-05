from pyramid.view import view_config
from utils import base_layout
from core import forum_svc, question_svc


@view_config(renderer="../templates/home.pt")
def index(request):
	questions = forum_svc.get_questions()
	return {"questions": questions, "layout": base_layout()}


@view_config(renderer="../templates/home.pt", name='search')
def search(request):
	search_term = request.GET['search']
	return {"questions": forum_svc.search(search_term), "layout": base_layout()}
	