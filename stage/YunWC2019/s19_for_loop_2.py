from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/for_loop_2',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'For Loop (2)',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '47'
    ],
    'code': [
        'numbers = [3, 10, 6, 4, 15, 9]',
        'sum = 0',
        '',
        '_____ n in _____:',
        '    sum += _____',
        '',
        'print(sum)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['47']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
