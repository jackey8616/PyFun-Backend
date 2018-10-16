from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/two/default_parameter',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Default parameter',
    'author': 'sean2525',
    'description': [
        'You can give a default param when you define a function.',
        '\n',
        '>>> def foo(v1, v2=1):',
        '...     print(v2)',
        '...',
        '>>> foo(0)',
        '1',
        '\n',
        'However, there can be no non-default parameters after the default parameters.',
        '\n',
        '>>> def foo2(v1=1, v2):',
        '...     print(v1)',
        '...',
        '  File "<stdin>", line 1',
        'SyntaxError: non-default argument follows default argument',
        '\n',
        '>>> def foo3(v1=1, v2=2):',
        '...     print(v1)',
        '...',
        '>>> foo3()',
        '1',
        '\n',
        'Now let\'s do an exercise.',
        '\n',
        'First, use the foo function to print "foo", at the same time avoiding foo2 error,',
        'Second, got that error.'
    ],
    'code': [
        'def foo(v1, _____ = "foo"):',
        '    print(_____)',
        'foo(0)',
        'def foo2(v1 = "foo2", _____):',
        '    print(v1)',
        'foo2()',
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
            return stderr[-1].decode() == 'SyntaxError: non-default argument follows default argument\n'
        else:
            return stdout[0].decode() == 'foo\n'
    except Exception:
        return False
