import connection_factory
from bson.objectid import ObjectId


def get_question(question_id):
    db = connection_factory.create()
    question = db.questions.find_one({'_id': ObjectId(question_id)})
    return question


def get_question_answers(question_id):
    db = connection_factory.create()
    answers = db.answers.find({'question_id': ObjectId(question_id)}).sort('votes', -1)
    return answers


def save_answer(question_id, answer):
    db = connection_factory.create()
    answer_id = db.answers.insert({'answer': answer, 'votes': 0, 'question_id': ObjectId(question_id)})
    question = db.questions.find_one(ObjectId(question_id))
    question['answers'].append(answer_id)
    db.questions.save(question)
    return answer_id


def vote(answer_id, vote):
    db = connection_factory.create()
    answer = db.answers.find_one({'_id': ObjectId(answer_id)})
    if vote == 'UP':
        answer['votes'] += 1
    else:
        answer['votes'] -= 1

    db.answers.save(answer)
    return answer['votes']
