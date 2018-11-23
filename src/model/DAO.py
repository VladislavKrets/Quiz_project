import postgresql


class DAO(object):
    def __init__(self):
        self.db = postgresql.open('pq://postgres:1234@localhost:5432/quiz_project')

    def getUsers(self):
        return self.db.query('select * from users')

    def isUserInDb(self, username, password):
        return self.db.query('select * from users where username=\'{}\' and password=\'{}\';'.format(username, password))

    def checkToken(self, token):
        return self.db.query('select * from tokens where token=\'{}\' and is_filled=\'false\';'.format(token))

    def getQuizByQuizId(self, quizId):
        return self.db.query('select * from quizes where quiz_id=\'{}\';'.format(quizId))

    def getQuestionsByQuizId(self, quizId):
        return self.db.query('select * from questions where quiz_id=\'{}\';'.format(quizId))

    def getAnswersByQuizIdAndQuestionId(self, quizId, questionId):
        return self.db.query('select * from answers where quiz_id=\'{}\' and question_id=\'{}\';'.format(quizId, questionId))

    def setTokenAlreadyUsed(self, token):
        self.db.prepare('update tokens set is_used=\'true\' where token=\'{}\';'.format(token))

    def writeUserAnswerToDb(self, quizId, questionId, answerId, type, answer=''):
        self.db.prepare('insert into user_request (quiz_id, question_id, answer_id, \'type\', answer) values (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(quizId, questionId, answerId, type, answer))