from flask import Flask, render_template, url_for, redirect, request

from src.model.DAO import DAO

app = Flask(__name__, template_folder='../view/quiz')
dao = DAO()


@app.route('/quiz/<token>', methods=['GET'], ['POST'])
def checkToken(token):
    tokenEntity = dao.checkToken(token)
    if len(tokenEntity) != 0:
        quiz = dao.getQuizByQuizId(tokenEntity['quiz_id'])
        questions = dao.getQuestionsByQuizId(tokenEntity['quiz_id'])
        answers = dict()
        for question in questions:
            answers[question["id"]] = dao.getAnswersByQuizIdAndQuestionId(quiz['quiz_id'], question['question_id'])
        if request.method == 'GET':
            return render_template('Quiz.html', quiz=quiz, questions=questions, answers=answers)
        else:
            # todo
            return render_template('QuizEnding.html')
    else:
        return redirect(url_for('error'))


@app.route('/error', methods=['GET'])
def quiz():
    return render_template('Error.html')


@app.route('/apply', methods=['POST'])
def quizApply():
    return 'QuizEnding'


app.run()
