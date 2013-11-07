import time
from core import question_svc
from test_stub import MongoTestCase, create_mock_collection


class TestQuestionCore(MongoTestCase):
    def test_get_question_by_id(self):
        c = create_mock_collection()
        question = {'title': 'question_mock',
                    'text': 'lorem ipsum...',
                    'tags': ['mock', 'test', 'python'],
                    'votes': 0}

        question_id = c.questions.insert(question)

        question_from_db = question_svc.get_question(question_id.__str__())

        self.assertEqual(question_id, question_from_db['_id'])

    def test_get_question_answers(self):
        c = create_mock_collection()
        question = {'title': 'question_mock',
                    'text': 'lorem ipsum...',
                    'tags': ['mock', 'test', 'python'],
                    'votes': 0}

        question_id = c.questions.insert(question)

        for i in range(5):
            answer = {'answer': 'answer%s' % i, 'votes': 0, 'question_id': question_id}
            c.answers.insert(answer)

        time.sleep(0.5)
        answers = question_svc.get_question_answers(question_id.__str__())
        self.assertEqual(5, answers.count())
        self.assertEqual('answer0', answers[0]['answer'])

    def test_save_answer(self):
        c = create_mock_collection()
        question = {'title': 'question_mock',
                    'text': 'lorem ipsum...',
                    'tags': ['mock', 'test', 'python'],
                    'votes': 0,
                    'answers': []}

        question_id = c.questions.insert(question)

        answer_id = question_svc.save_answer(question_id.__str__(), 'answer')

        answer = c.answers.find_one()
        self.assertEqual(answer_id, answer['_id'])

        question = c.questions.find_one({'_id': question_id})
        self.assertEqual(question['answers'][0], answer['_id'])

    def test_vote_answer(self):
        c = create_mock_collection()
        question = {'title': 'question_mock',
                    'text': 'lorem ipsum...',
                    'tags': ['mock', 'test', 'python'],
                    'votes': 0,
                    'answers': []}

        question_id = c.questions.insert(question)

        answer_id = c.answers.insert({'answer': 'answer', 'votes': 0, 'question_id': question_id})
        time.sleep(0.5)

        for i in range(1, 6):
            vote_numbers = question_svc.vote(answer_id.__str__(), 'UP')
            self.assertEqual(i, int(vote_numbers))

        answer = c.answers.find_one({'_id': answer_id})
        self.assertEqual(5, answer['votes'])

        vote_numbers = question_svc.vote(answer_id.__str__(), 'DOWN')
        answer = c.answers.find_one({'_id': answer_id})
        self.assertEqual(4, answer['votes'])
