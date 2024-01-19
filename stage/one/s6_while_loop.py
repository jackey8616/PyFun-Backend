from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/while_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'While Loop',
    'author': 'rozig',
    'description': [
        'Let\'s print 1 to 10 in descending order.',
        'Fill the missing fields!'
    ],
    'code': [
        'indicator = 10',
        '_____ 0 < indicator:',
        '    print(_____)',
        '    indicator -= 1'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['10\n', '9\n', '8\n', '7\n', '6\n', '5\n',
                   '4\n', '3\n', '2\n', '1\n']
            for each in range(0, 10):
                if stdout[each] != ans[each]:
                    return False
            return True
    except Exception:
        return False
