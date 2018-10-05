from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/two/list_comprehensions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Python List Comprehensions',
    'description': [
        'Let\'s learn about list comprehensions!',
        'In Python, list comprehensions combine the `list` and `for loop` ' +
        'to generate a list of objects created by the loop.',
        'You can reference list comprehension methods here: ' +
        'https://docs.python.org/3/tutorial/datastructures.html',
        '\n',
        'Now lets work on some exercises. You want to generate the ' +
        'following list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], but ' +
        'your fingers hurt so much that you do not want to type ' +
        'each item in the list!',
        'Use a list comprehension to generate this list.'
    ],
    'code': [
        'list_ = [x _____ x _____ _____(_____)]',
        'print(str(list_))'
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
            ans = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
            if stdout[0].decode() != ans:
                return False
            return True
    except Exception:
        return False
