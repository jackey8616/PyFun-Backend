from utils.form import blank_form
from utils import fields_generate


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

    ],
    'fields': []
}

data['fields'] = fields_generate(data)  # NEVER remove this line!!


async def sanic_request(request):
    try:
        return override(request)
    except NameError:
        global data, route
        return route['type'](data, request, answer)


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return True
    except Exception:
        return False
