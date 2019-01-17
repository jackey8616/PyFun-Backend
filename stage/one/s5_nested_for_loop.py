from utils.form import blank_form
from utils import fields_generate


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
            if len(stdout) != 5:
                return False
            ans = ['*****\n', '****\n', '***\n', '**\n', '*\n']
            for each in range(0, 5):
                if stdout[each].decode() != ans[each]:
                    return False
            return True
    except Exception:
        return False
