import connection_factory


def get_questions():
    db = connection_factory.create()
    questions = db.questions.find()
    return questions


def search(search_term):
    db = connection_factory.create()
    questions = db.questions.find({'tags': search_term})
    return questions
