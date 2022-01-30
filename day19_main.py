from day19_question import Question

q = ['1 + 3 = ?\n(a) 2\n(b) 3\n(c) 4\n',
     'what is the color of banana?\n(a) red\n(b) yellow\n(c) blue\n',
     'what is this editor?\n(a) vscode\n(b) vim\n(c) codeblocks\n']

questions = [Question(q[0], 'c'), Question(q[1], 'b'), Question(q[2], 'a')]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    print('you gain ' + str(score) + ' scores, totally '
        + str(len(questions)) + ' questions')

run_test(questions)

# print(nothing)
from day19_question import nothing
print(nothing)