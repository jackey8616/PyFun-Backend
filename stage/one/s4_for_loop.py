from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/for_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'For Loop',
    'author': 'Official',
    'description': [
        'I like A.P. (Arithmetic Progression)',
        'Can you give me a A.P. with five numbers,',
        'And each difference is 2.'
    ],
    'code': [
        'for each in range(_____, _____, _____):',
        '    print(each)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            if len(stdout) != 5:
                return False
            for each in range(1, len(stdout) - 1):
                if int(stdout[each]) - int(stdout[each - 1]) != 2:
                    return False
            return True
    except Exception:
        return False
