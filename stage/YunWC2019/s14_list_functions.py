from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/list_functions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'List Functions',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '[\'a\', \'b\', \'c\', \'e\']', '[\'a\', \'b\', \'c\', \'d\', \'e\']',
        '5', '2'
    ],
    'code': [
        'numbers = [\'a\', \'b\', \'c\']',
        'numbers._____(\'e\')',
        'print(numbers)',
        'numbers.insert(_____,_____)',
        'print(numbers)',
        'print(_____(numbers))',
        'print(numbers._____(\'c\'))'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['[\'a\', \'b\', \'c\', \'e\']', 
                   '[\'a\', \'b\', \'c\', \'d\', \'e\']', '5', '2']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
