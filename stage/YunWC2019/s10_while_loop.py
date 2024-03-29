from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/while_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'While Loop',
    'author': 'Official',
    'description': [
        'Print me a result like below.',
        '填滿空格, 然後印出下列結果:',
        '5', '4', '3', '2', '1', '0', '10'
    ],
    'code': [
        'num = _____',
        '',
        '_____ num > 0:',
        '    num -= 1',
        '    print(num)',
        '',
        'print(num + _____)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['5', '4', '3', '2', '1', '0', '10']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
