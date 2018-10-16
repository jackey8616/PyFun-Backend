from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/two/comment',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Comment',
    'author': 'stavhaygn',
    'description': [
        'What is a comment?',
        'Commments are added with the purpose of making the source code easier for humans to understand,',
        'and are generally ignored by interpreters in Python.',
        '',
        'Python doesn\'t have support for multi-line comments,',
        'but you can use multi-line strings as multi-line comments',
        '',
        'Now, let\'s finish this practice.',
        'Hint: No stdout and stderr',
    ],
    'code': [
        '_____ I am a comment',
        '',
        '_____',
        'print(\'QQ\')',
        'print(\'I am so tired\')',
        'print(\'I need a hug\')',
        '_____',
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
        if stderr == [] and stdout == []:
            return True
        return False
    except Exception:
        return False
