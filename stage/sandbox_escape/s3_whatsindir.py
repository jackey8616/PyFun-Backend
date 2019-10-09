from os import listdir

from utils.form import blank_form
from utils import fields_generate

route = {
    'type': blank_form,
    'url': '/stage/sandbox_escape/whatsindir',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'whats in dir',
    'author': 'Official',
    'description': [
        'Whhats in dir?',
        '這裡有什麼？'
    ],
    'code': [
        '_____("Ha Ha Ha'
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
            return stdout[0].decode() == "{}\n".format(listdir())
    except Exception:
        return False
