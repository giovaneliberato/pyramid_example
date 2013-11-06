import time
from core import forum_svc
from test_stub import MongoTestCase, create_mock_collection


class TestForumCore(MongoTestCase):
    def test_save_question(self):
        c = create_mock_collection()
        for i in range(5):
            question = {'title': 'question_mock%s' % i,
                        'text': 'lorem ipsum...',
                        'tags': ['mock', 'test', 'python'],
                        'votes': 0}

            c.questions.insert(question)

        questions_from_db = forum_svc.get_questions()

        time.sleep(0.4)

        self.assertEqual(5, questions_from_db.count())
        self.assertEqual('question_mock0', questions_from_db[0]['title'])

    def test_search_by_tag(self):
        c = create_mock_collection()
        for i in range(3):
            question = {'title': 'question_mock%s' % i,
                        'text': 'lorem ipsum...',
                        'tags': ['mock', 'test', 'python'],
                        'votes': 0}

            c.questions.insert(question)

        for i in range(2):
            question = {'title': 'question_mock%s' % i,
                        'text': 'lorem ipsum...',
                        'tags': ['stub', 'java', 'ruby'],
                        'votes': 0}

            c.questions.insert(question)

        time.sleep(0.4)

        found_questions = forum_svc.search('python')
        self.assertEqual(3, found_questions.count())
        self.assertEqual('question_mock0', found_questions[0]['title'])

        found_questions = forum_svc.search('stub')
        self.assertEqual(2, found_questions.count())
        self.assertEqual('question_mock0', found_questions[0]['title'])
