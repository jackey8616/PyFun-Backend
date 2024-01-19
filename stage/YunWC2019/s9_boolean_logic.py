from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/boolean_logic',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Boolean Logic',
    'author': 'Official',
    'description': [
        'True or False or True or False.',
        'Can you let these results be Good?',
        '010101001101011，數位邏輯好討厭ㄋㄧ',
        '填滿空格, 我想看到"Good!"的結果！'
    ],
    'code': [
        'score = _____',
        'if score >= 90 and score <= 100:',
        '    print("Good!")',
        '',
        'age = 20',
        'money = 300',
        '',
        'if age > 26 _____ money > 100:',
        '    print("Good!")',
        '',
        'if not _____:',
        '    print("Bad!")',
        'elif not (2+2 _____ 4):',
        '    print("Good!")',
        'else:',
        '    print("Bad")'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['Good!', 'Good!', 'Good!']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
