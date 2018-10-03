
import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'for_loop_2',
    'url': '/stage/one/for_loop_2',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'For Loop (2)',
    'description': [
        'This time I want some stars in triangle.',
        'Please give me a UP-SIDE-DOWN triangle stars with both width and height in 5.'
    ],
    'code': [
        'for each in range(0, _____):',
        '    for every in range(_____, 50):',
        '       print(\'*\', end=\'\')',
        '    print(\'\')'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)

async def for_loop_2(request):
    try:
        if request.method == 'GET':
            global data
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(data, request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr }})
    except:
        return json({ 'fail': True, 'data': traceback.format_exc() })

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            if len(stdout) != 5:
                return False
            ans = ['*****\n', '****\n', '***\n', '**\n', '*\n']
            for each in range(0, 5):
                if stdout[each].decode() != ans[each]:
                    return False
            return True
    except:
        return False
            
