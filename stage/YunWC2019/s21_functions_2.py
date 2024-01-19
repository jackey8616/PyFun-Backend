from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/functions_2',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Functions (2)',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '30'
    ],
    'code': [
        'def add(x, _____):',
        '    _____ x + y',
        '',
        'print(add(_____, 20))'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['30']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
