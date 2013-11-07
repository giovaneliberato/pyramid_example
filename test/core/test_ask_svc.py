from core import ask_svc
from core import connection_factory
from test_stub import MongoTestCase


class TestAskCore(MongoTestCase):
    def test_save_question(self):
        question_to_save = {'title': 'question_mock',
                            'text': 'lorem ipsum...',
                            'tags': ['mock', 'test', 'python'],
                            'votes': 0}

        question_id = ask_svc.save_question(question_to_save)

        db = connection_factory.create()
        question = db.questions.find()[0]

        self.assertEqual(question_id, question['_id'])
        self.assertEqual(question_to_save['title'], question['title'])
