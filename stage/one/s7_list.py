import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'list',
    'url': '/stage/one/list',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Python List',
    'description': [
        'Lets get familiar with Python list.',
        'In Python, list is a collection which is ordered and mutable sequence of objects.',
        'You can reference list methods here: https://docs.python.org/3/tutorial/datastructures.html',
        '\n',
        'Now lets work on some exercises. You have a following list: [9, 1, 4, 7, 3, 0, 5]',
        'Sort the list first and then reverse it. You can\'t use sort with reverse argument.'
    ],
    'code': [
        'list_ = [9, 1, 4, 7, 3, 0, 5]',
        'list_._____()',
        'list_._____()',
        'print(str(list_))'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)


async def list(request):
    try:
        if request.method == 'GET':
            global data
            return json({'success': True, 'data': data})
        else:
            code_data = concat_code(data, request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({'success': True, 'data': {'result': result, 'stdout': stdout, 'stderr': stderr}})
    except:
        return json({'fail': True, 'data': traceback.format_exc()})


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = "[9, 7, 5, 4, 3, 1, 0]\n"
            if stdout[0].decode() != ans:
                return False
            return True
    except:
        return False
