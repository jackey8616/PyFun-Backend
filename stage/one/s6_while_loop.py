import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'while_loop',
    'url': '/stage/one/while_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'While Loop',
    'description': [
        'Lets print 1 to 10 in ascending order.',
        'Fill the fields that are missing!'
    ],
    'code': [
        'indicator = 10',
        '_____ 0 < indicator:',
        '    print(_____)',
        '    indicator -= 1'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)


async def while_loop(request):
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
            ans = ['10\n', '9\n', '8\n', '7\n', '6\n', '5\n', '4\n', '3\n', '2\n', '1\n']
            for each in range(0, 10):
                if stdout[each].decode() != ans[each]:
                    return False
            return True
    except:
        return False
