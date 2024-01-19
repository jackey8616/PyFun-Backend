from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/string',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'String',
    'author': 'stavhaygn',
    'description': [
        'Strings are sequences of character data.',
        'Do you know how to use strings in Python?',
        'Let\'s print 8, Hello, M4gic, ABC.',
    ],
    'code': [
        'string = \'abcdefgh\'',
        'print(_____(string))',
        '',
        'string = \'Hello World\'',
        'print(string._____()[0])',
        '',
        'string = \'Magic\'',
        'print(string._____(\'a\', \'4\'))',
        '',
        'string = \'\\x_____\\x_____\\x_____\'',
        'print(string)',
    ],
    'fields': []
}

data['fields'] = fields_generate(data)


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
            ans = ['8\n', 'Hello\n', 'M4gic\n', 'ABC\n']
            if len(stdout) != len(ans):
                return False
            for index in range(0, len(ans)):
                if stdout[index] != ans[index]:
                    return False
            return True
    except Exception:
        return False
