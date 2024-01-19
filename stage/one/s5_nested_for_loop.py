from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/nested_for_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Nested For Loop',
    'author': 'Official',
    'description': [
        'This time I want some stars in triangle.',
        'Please give me a UP-SIDE-DOWN triangle stars with both width ' +
        'and height in 5.'
    ],
    'code': [
        'for each in range(0, _____):',
        '    for every in range(_____, 50):',
        '        print(\'*\', end=\'\')',
        '    print(\'\')'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            if len(stdout) != 5:
                return False
            ans = ['*****\n', '****\n', '***\n', '**\n', '*\n']
            for each in range(0, 5):
                if stdout[each] != ans[each]:
                    return False
            return True
    except Exception:
        return False
