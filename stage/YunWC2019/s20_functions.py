from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/functions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Functions',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        'Hi'
    ],
    'code': [
        '_____ hello() _____',
        '    print(\'Hi\')',
        '',
        '_____()'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['Hi']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
