from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/import',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Import',
    'author': 'Official',
    'description': [
        'Yo!',
        'If you want to use pyperclip that is a package',
        'What command should you add ?'
    ],
    'code': [
        '_____(\'_____\')'
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
            return stdout[0].decode() == 'pyperclip\n'
    except Exception:
        return False
