from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/list_functions_2',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'List Functions (2)',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '[6, 5, 4, 3, 2, 1]'
    ],
    'code': [
        'numbers = [1, 6, 4, 5, 3, 2]',
        'numbers._____()',
        'numbers._____()',
        'print(numbers)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['[6, 5, 4, 3, 2, 1]']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
