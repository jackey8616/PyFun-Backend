from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/if_elif_else',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'If ElseIf and Else',
    'image': 'https://myanimelist.cdn-dena.com/images/characters/6/276027.jpg',
    'description': [
        'Do you know Haruna?',
        'If you know her, then you are my friend.'
    ],
    'code': [
        'answer = _____',
        'if answer == \'I know her\':',
        '    print(\'We are best friend.\')',
        'elif answer == \'Who is she?\':',
        '    print(\'You are not my friend! go away!\')',
        'else:',
        '    print(\'May be you can understand who she is right now.\')'
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
            return True
    except Exception:
        return True
