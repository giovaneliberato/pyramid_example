from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from utils import base_layout


@view_config(renderer="../templates/ask.pt", name='ask')
def ask(request):
    return {"layout": base_layout()}

@view_config(name='save_question')
def save_question(request):
	db = connection_factory.create()
	params_dict = request.params.mixed()
	params_dict['tags'] = params_dict['tags'].split(',')
	params_dict['votes'] = 0
	question_id = db.questions.insert(params_dict)
	red = 'question?id=%s' % question_id
	return HTTPFound(location=red)
