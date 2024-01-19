from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/string_operations',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'String Operations',
    'author': 'Official',
    'description': [
        'Asuka Meow meow meow meow meow!',
        'Print me with "Cute cat! meow~ meow~ meow~"',
        '喵喵喵喵喵喵喵喵喵喵',
        '請喵給我"Cute cat! meow~ meow~ meow~"'
    ],
    'code': [
        'print("Cute cat!" _____ " meow~" _____)'
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
            return stdout[0] == 'Cute cat! meow~ meow~ meow~\n'
    except Exception:
        return False
