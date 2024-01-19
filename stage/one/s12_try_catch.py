from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/try_catch',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Try Catch',
    'author': 'b3_900d',
    'description': [
        'This is error handling lesson with try catch.\n',
        'If you want ignore the specific exception,\n',
        ' just add pass to the except part',
    ],
    'code': [
        'try:',
        '    dividend_number = _____',
        '    divisor_number = 0',
        'except ZeroDivisionError:',
        '    print(\'The message appear because we have divisor 0\')',
        'try:',
        '    dividend_number = _____',
        '    divisor_number = 0',
        'except ZeroDivisionError:',
        '    # This will do nothing',
        '    pass',

    ]
}


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return True
    except Exception:
        return False
