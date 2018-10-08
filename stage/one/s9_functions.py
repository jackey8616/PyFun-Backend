from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/functions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Functions',
    'author': 'Oshawk',
    'description': [
        'Functions are where Python start to become really powerful.',
        'They provide a simple way to divide your code into sections or ' +
        'easily perform common tasks. Say for example we have a program that' +
        ' needs to check of a lot of integers are odd. It may save time in ' +
        'the long term to make an "is_odd" function. This may look like:',
        '',
        'def is_odd(num):',
        '    if num % 2 == 0:',
        '        return False',
        '    else:',
        '        return True',
        '',
        'As you can see we start the function with the "def" keyword ' +
        'followed by the function name. Next comes a set of brackets with ' +
        'the arguments for the function followed by a colon and the code.',
        'The "return" keyword says what we want to give back to the user ' +
        'running the function. To call a function, state the function name ' +
        'followed by brackets containing what you wish to pass in. ' +
        'E.g. "is_odd(23)" which returns "True".',
        'Now try to fill in the blanks below!!!'
    ],
    'code': [
        'def add(_____, _____):',
        '     _____ num1 + num2',
        '',
        'if add(1, 2) == 3:',
        '    print("Well done!")',
        'else:',
        '    print("Sorry, that is wrong.")'
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
            ans = 'Well done!\n'
            if stdout[0].decode() != ans:
                return False
            return True
    except Exception:
        return False
