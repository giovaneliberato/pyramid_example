import connection_factory


def save_question(question):
    db = connection_factory.create()
    question['answers'] = []
    question_id = db.questions.insert(question)
    return question_id
