from utils.form import blank_form
from utils import fields_generate

route = {
    'type': blank_form, 
    'url': '/stage/two/slicing',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Slicing',
    'image': 'https://i.stack.imgur.com/o99aU.png',
    'author': 'sean2525',
    'description': [
        'Python has an amazing feature just for that called slicing.',
        'Slicing can not only be used for lists, tuples or arrays,' +
        'but custom data structures as well.',
        'It can be used like: list[start:end:increment]',
        '>>> a = [1, 2, 3, 4]',
        '>>> a[1:2]',
        '[2, 3]'
        '>>> a[1:]',
        '[2, 3, 4]',
        '>>> a[::-1]',
        '[4, 3, 2, 1]',
        'Now let\'s do an exercise.',
        '\n'
        'There is a list: [0, 1, 2, 3, 6, 7, 8, 4, 5, 9, 10],',
        'I want to generate [4, 8, 7, 6, 3] by slicing.',
        'But i don\'n know how to do it, can you help me?'
    ],
    'code': [
        'a = [0, 1, 2, 3, 6, 7, 8, 4, 5, 9, 10]',
        'print(a[_____:_____][::_____])',
        '# Also try this',
        'print(a[_____:_____:_____])'
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

# If you don't want to use any type of those.
# You can write yourself one, just properly handle Sanic request.
# **IMPORTANT** Unless you are sure to use customize one, or do not comment out this function.
# def override(request):
#     pass

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0].decode() == '[4, 8, 7, 6, 3]\n'
    except:
        return False
